import timeit
from TSP_A_STAR import find_shortest_path_a_star
from TSP_BFS import find_shortest_path_bfs
from TSP_UCS import find_shortest_path_ucs


# Calcularea timpului de executie
def measure_execution_time(func, *args):
    start_time = timeit.default_timer()  # Timpul de start
    result = func(*args)  # Executarea functiei cu argumentele date
    end_time = timeit.default_timer()  # Timpul de sfarsit
    execution_time = end_time - start_time  # Calcularea timpului de executie
    return result, execution_time


if __name__ == "__main__":
    distances = {
        'A': {'B': 3, 'C': 9, 'D': 5, 'E': 7},
        'B': {'A': 3, 'C': 8, 'D': 6, 'E': 2},
        'C': {'A': 9, 'B': 8, 'D': 4, 'E': 1},
        'D': {'A': 5, 'B': 6, 'C': 4, 'E': 9},
        'E': {'A': 7, 'B': 2, 'C': 1, 'D': 9}
    }

    start_city = "A"  # Orasul de start

    # Afisarea distantelor intre orase
    print("\nDistances between cities:")
    for city, neighbours in distances.items():
        distances_str = ", ".join([f"{neighbour}: {distance} km" for neighbour, distance in neighbours.items()])
        print(f"{city} -> {distances_str}")

    # Afisarea orasului de pornire
    print(f"\nStarting city: {start_city}")

    # Algoritmul A*
    (cost_a_star, path_a_star), execution_time_a_star = measure_execution_time(find_shortest_path_a_star, start_city,
                                                                               distances)
    print(f"\nShortest path cost (A*): {cost_a_star}")
    print("Path (A*):", " -> ".join(path_a_star))
    print(f"Execution time (A*): {execution_time_a_star:.10f} seconds")

    # Algoritmul BFS
    (cost_bfs, path_bfs), execution_time_bfs = measure_execution_time(find_shortest_path_bfs, start_city, distances)
    print(f"\nShortest path cost (BFS): {cost_bfs}")
    print("Path (BFS):", " -> ".join(path_bfs))
    print(f"Execution time (BFS): {execution_time_bfs:.10f} seconds")

    # Algoritmul UCS
    (cost_ucs, path_ucs), execution_time_ucs = measure_execution_time(find_shortest_path_ucs, start_city, distances)
    print(f"\nShortest path cost (UCS): {cost_ucs}")
    print("Path (UCS):", " -> ".join(path_ucs))
    print(f"Execution time (UCS): {execution_time_ucs:.10f} seconds")
