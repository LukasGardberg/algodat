import sys
import heapq

line1 = sys.stdin.readline().split()


N = int(line1[0])  # Nbr of people
M = int(line1[1])  # Nbr of edges

dists = [[-1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    line = sys.stdin.readline().split()
    dists[int(line[0]) - 1][int(line[1]) - 1] = dists[int(line[1]) - 1][int(line[0]) - 1] = int(line[2])

q = [(float('inf'), None) for _ in range(N - 1)]


heapq.heapify(q)
print(heapq.heappop(q))
print(q)