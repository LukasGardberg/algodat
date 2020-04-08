import sys

line1 = sys.stdin.readline().split()

N = int(line1[0])
Q = int(line1[1])


# Def node class
class Node:

    def __init__(self, word):
        self.neighbors = []
        self.word = word

    def add_neighbor(self, node):
        self.neighbors.append(node)


# Read in words and store in nodes
words = [Node(sys.stdin.readline().strip()) for _ in range(N)]


def connected(node1, node2):
    # returns if node1 and node2 should be connected
    string1 = node1.word[1:]
    string2 = node2.word

    for l in string1:
        if l in string2:
            string2 = string2.replace(l, '', 1)
        else:
            return False

    return True


for word in words:
    temp_node = Node(word)


def bfs(start, stop):
    visited = set()




    pass


