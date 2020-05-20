import sys

line1 = sys.stdin.readline().split()

cost = [[int(j) for j in sys.stdin.readline().split()] for _ in range(len(line1))]

n_queries = int(sys.stdin.readline())

gap_pen = -4

# build map with letter indices
letter_index = {letter: nbr for (letter, nbr) in zip(line1, range(len(line1)))}


def optimal_alignment(string1, string2):
    n = len(string1)
    m = len(string2)

    # contains the optimal alignment score for substrings s1[:i], s2[:j] in A[i,j]
    substr_score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # add scores for just inserting gaps
    substr_score[0] = [i * gap_pen for i in range(n + 1)]

    for i in range(m + 1):
        substr_score[i][0] = gap_pen * i

    # calculate optimal alignment scores
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # get score for matching both letters
            match = substr_score[i-1][j-1] + cost[letter_index[string1[j-1]]][letter_index[string2[i-1]]]

            # score for '*' in string 1
            gap_s1 = substr_score[i][j-1] + gap_pen

            # score for '*' in string 2
            gap_s2 = substr_score[i-1][j] + gap_pen

            substr_score[i][j] = max(match, gap_s1, gap_s2)

    print(substr_score)

optimal_alignment('ABA', 'ACA')
