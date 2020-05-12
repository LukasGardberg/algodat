import sys
import time

# Solver for lab 2 in EDAF05
# Improvements: replace the word_map with a matrix and index words with integers instead.

# Read input
line1 = sys.stdin.readline().split()

N = int(line1[0])   # Nbr of words
Q = int(line1[1])   # Nbr queries

# Read in words and store in a (key, val) = (word, neighbors) map.
word_map = {}

for i in range(N):
    word_map[sys.stdin.readline().strip()] = []


# Function to determine if two words should be connected
def connected(word1, word2):
    # returns true if word1 should have an edge to word2
    for char in word1[1:]:
        if char in word2:
            word2 = word2.replace(char, '', 1)
        else:
            return False

    return True


# Store the correct neighbors to each word
for word1 in word_map:
    for word2 in word_map:
        if word1 != word2 and connected(word1, word2):
            word_map[word1].append(word2)


# Breadth first search algorithm
# input: start_w, stop_w words (string), returns: path_length (int) or 'Impossible'
def bfs(start_w, stop_w):
    # if the words are the same then path_length is 0
    if start_w == stop_w:
        return 0

    visited = {start_w}
    q = [start_w]
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
                if neighbor == stop_w:
                    # Found shortest
                    temp_neighbor = stop_w

                    # Calc path length
                    while parents[temp_neighbor] != start_w:
                        temp_neighbor = parents[temp_neighbor]
                        path_length += 1

                    return path_length

    return 'Impossible'


# Read in queries and print result
for _ in range(Q):
    line = sys.stdin.readline().split()
    start = line[0]
    stop = line[1]

    print(bfs(start, stop))

