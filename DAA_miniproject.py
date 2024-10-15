#Brute Force
import itertools

def calculate_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)) + distance_matrix[tour[-1]][tour[0]]

def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_tour = None
    min_distance = float('inf')
    
    for tour in itertools.permutations(cities):
        current_distance = calculate_distance(tour, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_tour = tour
            
    return min_tour, min_distance





#Dynamic Programming (Held-Karp)

def held_karp(distance_matrix):
    n = len(distance_matrix)
    C = {}
    
    for i in range(1, n):
        C[(1 << i, i)] = (distance_matrix[0][i], 0)

    for r in range(3, n + 1):
        for subset in itertools.combinations(range(1, n), r - 1):
            subset_mask = sum(1 << i for i in subset)
            for j in subset:
                prev_mask = subset_mask ^ (1 << j)
                C[(subset_mask, j)] = min((C[(prev_mask, k)][0] + distance_matrix[k][j], k) for k in subset if k != j)

    last_mask = (1 << n) - 1
    optimal_cost, last_city = min((C[(last_mask, j)][0] + distance_matrix[j][0], j) for j in range(1, n))
    return optimal_cost


#EXAMPLE USAGE
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Brute Force
print("Brute Force TSP:", brute_force_tsp(distance_matrix))

# Held-Karp
print("Dynamic Programming TSP Cost:", held_karp(distance_matrix))

# Nearest Neighbor
print("Nearest Neighbor TSP:", nearest_neighbor_tsp(distance_matrix))
