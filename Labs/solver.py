from pathlib import Path
import numpy as np

entries = Path(r'C:\Users\Lukas\PycharmProjects\algodat\EDAF05-labs-public-master\1stablemarriage\data\secret')

input_file = entries / '0testsmall.in'
input = open(input_file, 'r')

# number of men and women
n = int(input.readline())

men = np.zeros((n, n))
women = np.zeros((n, n))

lines = input.readlines()

# first occurring index is a woman
for line in lines:
    temp_arr = np.fromstring(line, dtype=int, sep=' ')
    index = temp_arr[0] - 1
    print(line)
    # Determine if woman of man
    if women[index, 0] == 0:
        # store array so that man i has ranking arr[i]
        for i in range(1, n+1):
            women[index, temp_arr[i] - 1] = i
    else:
        men[index, :] = temp_arr[1:]

print(women)
print(men)