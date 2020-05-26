import sys
from collections import defaultdict

line1 = sys.stdin.readline().split()

n_nodes = int(line1[0])
n_edges = int(line1[1])
flow_demand = int(line1[2])  # number of students
n_routes = int(line1[3])

capacities = defaultdict(list)

adj = [[-1 for _ in range(n_nodes)] for _ in range(n_nodes)]

# dictionary for node neighbors and capacity of edges
for _ in range(n_edges):
    # Store in dict
    node1, node2, capacity = sys.stdin.readline().split()
    node1 = int(node1)
    node2 = int(node2)
    capacity = int(capacity)

    capacities[node1].append(node2)
    capacities[node2].append(node1)

    # Store in adj. matrix
    adj[node1][node2] = adj[node2][node1] = capacity


# BFS algorithm, node_dict assumed dictionary node_int: [(node_int, cap), ..]


def bfs(node_dict, adj_matrix):
    start_node = 0
    stop_node = n_nodes - 1

    visited = {start_node}
    q = [start_node]
    parents = {}

    while q:
        current_node = q.pop(0)

        # Generator expression
        gen = (neighbor for neighbor in node_dict[current_node] if adj_matrix[neighbor][current_node] > 0)

        for neighbor in gen:
            # if neighbor has not been visited then add it to visited and append neighbor to q
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                parents[neighbor] = current_node
                if neighbor == stop_node:
                    # Found path
                    temp_node = stop_node

                    # Find path back, return smallest capacity
                    min_cap = float("inf")
                    path = [stop_node]
                    while parents[temp_node] != start_node:
                        # add node to path
                        path.insert(0, parents[temp_node])

                        # find min capacity along path
                        temp_cap = adj_matrix[temp_node][parents[temp_node]]

                        if temp_cap < min_cap:
                            min_cap = temp_cap

                        temp_node = parents[temp_node]
                    # Add start node to path
                    path.insert(0, start_node)

                    # Check last capacity to start node
                    temp_cap = adj_matrix[temp_node][start_node]

                    if temp_cap < min_cap:
                        min_cap = temp_cap

                    return path, min_cap
    # No path was found
    return False

# Ford Fulkeson algorithm, outputs max flow in graph node_dict


def ford_fulk(node_dict, adj_matrix):


    while temp_tuple := bfs(capacities, adj):
        path = temp_tuple[0]
        min_cap = temp_tuple[1]




