import sys
import heapq
import time

t_read = time.time()

line1 = sys.stdin.readline().split()

N = int(line1[0])  # Nbr of people
M = int(line1[1])  # Nbr of edges

dists = [[-1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    line = sys.stdin.readline().split()
    dists[int(line[0]) - 1][int(line[1]) - 1] = dists[int(line[1]) - 1][int(line[0]) - 1] = int(line[2])

t_read = time.time() - t_read

t_makeheap = time.time()

root = 0
total_dist = 0

mst = set()
visited = {root}

Q = []

# Add distances and edges from root to heapq
for i in range(N):
    d = dists[root][i]
    if d != -1:
        Q.append((d, root, i))

heapq.heapify(Q)

t_makeheap = time.time() - t_makeheap

t_solve = time.time()

while Q:
    # Pop nearest vertex from our MST
    dist, frm, to = heapq.heappop(Q)

    if to not in visited:
        visited.add(to)

        total_dist += dist

        # Check next edges to consider
        for i in range(N):
            d_temp = dists[to][i]
            if i not in visited and d_temp != -1:
                heapq.heappush(Q, (d_temp, to, i))

t_solve = time.time() - t_solve

print('reading time ', t_read)
print('heap making time ', t_makeheap)
print('solving time ', t_solve)


print(total_dist)