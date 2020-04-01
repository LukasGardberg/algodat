from pathlib import Path

# Det här är ett dåligt sätt eftersom vi har olika filsökvägar på olika maskiner
# entries = Path(r'C:\Users\Lukas\PycharmProjects\algodat\EDAF05-labs-public-master\1stablemarriage\data\secret)

# Det här är ett bättre sätt
entries = Path(__file__).parent.parent.parent / 'EDAF05-labs-public-master' / '1stablemarriage' / 'data' / 'secret'

input_file = entries / "0testsmall.in"
input = open(input_file, 'r')

# number of men and women
n = int(input.readline())

men = [{'preferences': [], 'proposals': 0, 'is_engaged': False} for i in range(n)]
women = [{'preferences': [], 'partner': 0, 'is_engaged': False} for i in range(n)]

lines = input.readlines()

# first occurring index is a woman
for line in lines:
    temp_arr = [int(x) for x in line.split()]  # så här slipper man numpy
    index = temp_arr[0] - 1
    print(line)
    # Determine if woman or man
    if not women[index]['preferences']:
        # for women store inverted array
        w_pref = [0] * n
        for i in range(1, n+1):
            w_pref[temp_arr[i] - 1] = i

        women[index]['preferences'] = w_pref
    else:
        # for men store array as normal
        men[index]['preferences'] = temp_arr[1:]
