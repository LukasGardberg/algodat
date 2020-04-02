import sys

n = int(sys.stdin.readline())

lines = sys.stdin.readlines()

men = [{'preferences': [], 'proposals': 0} for i in range(n)]
women = [{'preferences': [], 'partner': 0, 'is_engaged': False} for i in range(n)]

# first occurring index is a woman
for line in lines:
    temp_arr = [int(x) for x in line.split()]
    index = temp_arr[0] - 1

    # Determine if woman or man
    if not women[index]['preferences']:
        # for women store inverted array
        w_pref = [0 for i in range(n)]
        for i in range(1, n+1):
            w_pref[temp_arr[i] - 1] = i - 1

        women[index]['preferences'] = w_pref
    else:
        # for men store array as normal

        men[index]['preferences'] = [x - 1 for x in temp_arr[1:]]

# Array (stack) of available men by index
p = [x for x in range(n)]

while p:
    m_index = p.pop()
    current_man = men[m_index]

    n_proposals = current_man['proposals']

    current_man['proposals'] += 1
    w_next_index = current_man['preferences'][n_proposals]

    current_woman = women[w_next_index]

    if not current_woman['is_engaged']:
        # m and w becomes a pair
        current_woman['is_engaged'] = True
        current_woman['partner'] = m_index

    elif current_woman['preferences'][m_index] < current_woman['preferences'][current_woman['partner']]:
        # w prefers current man over husband, add husband to p and make w and current man a pair
        p.append(current_woman['partner'])
        current_woman['partner'] = m_index

    else:
        p.append(m_index)

for i in range(n):
    print(women[i]['partner'] + 1)
