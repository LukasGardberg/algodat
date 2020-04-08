import sys

line1 = sys.stdin.readline().split()

N = int(line1[0])
Q = int(line1[1])

# Read in words and store in nodes
word_map = {}

for i in range(N):
    word_map[sys.stdin.readline().strip()] = []

def connected(word1, word2):
    # returns true if word1 has an edge to word2

    for char in word1[1:]:
        if char in word2:
            word2 = word2.replace(char, '', 1)
        else:
            return False

    return True


for word1 in word_map:
    for word2 in word_map:
        if word1 != word2 and connected(word1, word2):
            word_map[word1].append(word2)


def bfs(start, stop):
    visited = {start}
    q = [start]
    parents = {}
    path_length = 1

    while q:
        v = q.pop(0)
        for neighbor in word_map[v]:
            # if neighbor has not been visited then add it to visited and append neighbor to q
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                parents[neighbor] = v
                if neighbor == stop:
                    temp_neighbor = stop

                    while parents[temp_neighbor] != start:
                        temp_neighbor = parents[temp_neighbor]
                        path_length += 1

                    return path_length

    return 'Impossible'

for _ in range(Q):
    line = sys.stdin.readline().split()
    start = line[0]
    stop = line[1]

    print(bfs(start, stop))

