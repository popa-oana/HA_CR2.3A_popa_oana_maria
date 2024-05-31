import heapq


class NodeAStar:
    # Clasa pentru nodurile utilizate în algoritmul A*
    def __init__(self, city, visited, cost, estimated_cost, path):
        self.city = city  # Orasul curent
        self.visited = set(visited)  # Orasele vizitate
        self.cost = cost  # Costul actual al rutei
        self.estimated_cost = estimated_cost  # Costul estimat (heuristic)
        self.path = list(path)  # Calea urmata pana acum

    def __lt__(self, other):
        # Comparare intre noduri pentru a fi utilizate în coada de prioritati
        return (self.cost + self.estimated_cost) < (other.cost + self.estimated_cost)


def heuristic(current_city, visited, distances):
    # Functia heuristica pentru algoritmul A*
    min_distance = float('inf')
    for city in distances.keys():
        if city not in visited and city != current_city:  # Excludem orasul curent din calcul
            distance = distances[current_city].get(city, float('inf'))
            min_distance = min(min_distance, distance)
    return min_distance if min_distance != float('inf') else 0


def find_shortest_path_a_star(start_city, distances):
    # Gaseste calea de cost minim utilizand algoritmul A*
    pq = []
    heapq.heappush(pq, NodeAStar(start_city, {start_city}, 0, 0, [start_city]))

    min_cost = float('inf')
    min_path = []
    num_cities = len(distances)

    while pq:
        current_node = heapq.heappop(pq)

        if len(current_node.visited) == num_cities:
            # Verifica daca toate orasele au fost vizitate
            return_cost = distances[current_node.city].get(start_city)
            if return_cost:
                total_cost = current_node.cost + return_cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    min_path = current_node.path + [start_city]
            continue

        for next_city, next_cost in distances[current_node.city].items():
            if next_city not in current_node.visited:
                new_visited = set(current_node.visited)
                new_visited.add(next_city)
                new_path = list(current_node.path)
                new_path.append(next_city)
                est_cost = heuristic(next_city, new_visited, distances)
                heapq.heappush(pq, NodeAStar(next_city, new_visited, current_node.cost + next_cost, est_cost, new_path))

    return min_cost, min_path
