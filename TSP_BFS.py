from collections import deque


class NodeBFS:
    # Clasa pentru nodurile utilizate în algoritmul BFS
    def __init__(self, city, visited, cost, path):
        self.city = city  # Orasul curent
        self.visited = set(visited)  # Orasele vizitate
        self.cost = cost  # Costul actual al rutei
        self.path = list(path)  # Calea urmata pana acum


def find_shortest_path_bfs(start_city, distances):
    # Gaseste calea de cost minim utilizand algoritmul BFS
    queue = deque([NodeBFS(start_city, {start_city}, 0, [start_city])])

    min_cost = float('inf')
    min_path = []
    num_cities = len(distances)

    while queue:
        current_node = queue.popleft()

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
                queue.append(NodeBFS(next_city, new_visited, current_node.cost + next_cost, new_path))

    return min_cost, min_path
