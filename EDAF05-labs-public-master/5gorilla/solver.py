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

    # contains the optimal alignment score for substrings s1[:row], s2[:col] in A[row,col]
    substr_score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # add scores for just inserting gaps
    substr_score[0] = [i * gap_pen for i in range(n + 1)]

    for i in range(m + 1):
        substr_score[i][0] = gap_pen * i

    # calculate optimal alignment scores
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            # get score for matching both letters
            match = substr_score[row-1][col-1] + cost[letter_index[string1[col-1]]][letter_index[string2[row-1]]]

            # match opposing letter with '*' ('*' in string1)
            gap_s1 = substr_score[row][col-1] + gap_pen

            # match this letter with '*' ('*' in string2)
            gap_s2 = substr_score[row-1][col] + gap_pen

            substr_score[row][col] = max(match, gap_s1, gap_s2)

    # Backtrack and find correct optimal string alignment

    row = m
    col = n

    opt_string1 = ''
    opt_string2 = ''

    while row > 0 and col > 0:

        # if our score corresponds to matching both letters, add these to optimal strings
        if substr_score[row][col] == substr_score[row-1][col-1] + \
                cost[letter_index[string1[col-1]]][letter_index[string2[row-1]]]:
            opt_string1 = string1[col - 1] + opt_string1
            opt_string2 = string2[row - 1] + opt_string2

            row -= 1
            col -= 1
        # else if score corresponds to matching letter in string1 with '*' in string2, add to opt string
        elif substr_score[row][col] == substr_score[row][col-1] + gap_pen:
            opt_string1 = string1[col - 1] + opt_string1
            opt_string2 = '*' + opt_string2

            col -= 1
        # else (always) if score corresponds to matching letter in string 2 with '*' in string1, add to opt string
        elif substr_score[row][col] == substr_score[row-1][col] + gap_pen:
            opt_string1 = '*' + opt_string1
            opt_string2 = string2[row - 1] + opt_string2

            row -= 1
        else:
            print('somethings fucky')

    # Check if one of the strings are shorter than the other, and therefore needs spaces to align
    if row > 0:
        while row > 0:
            opt_string1 = '*' + opt_string1
            opt_string2 = string2[row - 1] + opt_string2
            row -= 1
    elif col > 0:
        while col > 0:
            opt_string2 = '*' + opt_string2
            opt_string1 = string1[col - 1] + opt_string1
            col -= 1

    return opt_string1, opt_string2


# read in queries and print
for _ in range(n_queries):
    line = sys.stdin.readline().split()
    str1, str2 = optimal_alignment(line[0], line[1])
    print(str1, str2)
