import sys
import heapq
import time
from collections import defaultdict

# Implementation of Prim's algorithm

t_read = time.time()

line1 = sys.stdin.readline().split()

N = int(line1[0])  # Nbr of people
M = int(line1[1])  # Nbr of edges

dists = defaultdict(list)

# Store adjacent nodes and edge weights in map
for _ in range(M):
    line = sys.stdin.readline().split()
    dists[int(line[0])].append((int(line[2]), int(line[1])))
    dists[int(line[1])].append((int(line[2]), int(line[0])))

t_read = time.time() - t_read

t_makeheap = time.time()

root = 1
total_dist = 0

visited = {root}

Q = []

# Add distances and edges from root to heapq
for dist, to in dists[root]:
    Q.append((dist, root, to))

heapq.heapify(Q)

t_makeheap = time.time() - t_makeheap

t_solve = time.time()

# Prim's algorithm
while Q:
    # Pop nearest vertex from our MST
    dist, frm, to = heapq.heappop(Q)

    if to not in visited:
        visited.add(to)

        total_dist += dist

        # Check next edges to consider
        for next_d, next_to in dists[to]:
            if next_to not in visited:
                heapq.heappush(Q, (next_d, to, next_to))


t_solve = time.time() - t_solve

# print('reading time ', t_read)
# print('heap making time ', t_makeheap)
# print('solving time ', t_solve)

print(total_dist)
