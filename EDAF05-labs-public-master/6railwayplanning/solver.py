import sys
from collections import defaultdict
import time

line1 = sys.stdin.readline().split()

n_nodes = int(line1[0])
n_edges = int(line1[1])
flow_demand = int(line1[2])  # number of students
n_routes = int(line1[3])

neighbors = defaultdict(list)

# Initialize adjacency matrix and residual graph
adj = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]
res_graph = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]

edges = [[0, 0] for _ in range(n_edges)]

# dictionary for node neighbors and capacity of edges
for i in range(n_edges):

    # Store in dict
    node1, node2, capacity = sys.stdin.readline().split()
    node1 = int(node1)
    node2 = int(node2)
    capacity = int(capacity)

    neighbors[node1].append(node2)
    neighbors[node2].append(node1)

    # Store in edge list
    edges[i] = [node1, node2]

    # Store in adj. matrix (obs, elementen i grafen är pekar på samma?)
    adj[node1][node2] = adj[node2][node1] = capacity

    # Store in residual graph (these are equal at the start)
    res_graph[node1][node2] = capacity
    res_graph[node2][node1] = capacity

# BFS algorithm, node_dict assumed dictionary node_int: [(node_int, cap), ..]
# input: node_dict, adjacency matrix.
# output: array of indices of path, min_capacity along that path
# OR false if no path was found.


def bfs(node_dict, adj_matrix):
    start_node = 0
    stop_node = n_nodes - 1

    # print(adj_matrix)
    # time.sleep(2)

    visited = {start_node}
    q = [start_node]
    parents = {}

    while q:
        current_node = q.pop(0)

        # Generator expression
        gen = (neighbor for neighbor in node_dict[current_node] if adj_matrix[current_node][neighbor] > 0)

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


def ford_fulk(node_dict, cap_matrix, curr_flow):
    # create empty flow matrix
    # flow_matrix = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]

    # duplicate adjacency matrix (residual graph?)
    # cap_matrix = [[cap for cap in adj_matrix[row][:]] for row in range(len(adj_matrix))]

    max_flow = curr_flow

    temp_tuple = bfs(node_dict, cap_matrix)

    while temp_tuple:
        path = temp_tuple[0]
        # print(path)
        min_cap = temp_tuple[1]

        max_flow += min_cap

        # Loop back through path and add flow
        for index in range(len(path) - 1):
            node_from = path[index]
            node_to = path[index + 1]

            # subtract flow from capacity
            cap_matrix[node_from][node_to] -= min_cap
            cap_matrix[node_to][node_from] += min_cap

        temp_tuple = bfs(node_dict, cap_matrix)

    return max_flow


# Read in queries
queries = [int(sys.stdin.readline()) for _ in range(n_routes)]

# Remove all edges in queries from res_graph
for query in queries:
    # Set capacity to 0 in both directions
    res_graph[edges[query][0]][edges[query][1]] = 0
    res_graph[edges[query][1]][edges[query][0]] = 0

# Do FF on graph with all requested edges removed
current_flow = ford_fulk(neighbors, res_graph, 0)

# Check if we are done
if current_flow >= flow_demand:
    print(n_routes, current_flow)
else:

    n_removed = n_routes
    potential_capacity = 0

    # Loop through queries
    for query in reversed(queries):
        n_removed -= 1

        node1 = edges[query][0]
        node2 = edges[query][1]

        cap_to_add = adj[node1][node2]

        res_graph[node1][node2] = cap_to_add
        res_graph[node2][node1] = cap_to_add

        potential_capacity += cap_to_add

        # only run FF if we are able to achieve demanded flow
        if potential_capacity + current_flow >= flow_demand:
            current_flow = ford_fulk(neighbors, res_graph, current_flow)

            # Reset potential capacity
            potential_capacity = 0
            # print(current_flow)

            # if we are done
            if current_flow >= flow_demand:
                break

    print(n_removed, current_flow)
