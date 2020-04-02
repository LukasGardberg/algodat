import sys
import time

n = int(sys.stdin.readline())
t1 = time.time()
lines = ' '.join(line.rstrip() for line in sys.stdin.readlines())
arr = [int(x) for x in lines.split()]

men = [{'preferences': [], 'proposals': 0} for i in range(n)]
women = [{'preferences': [], 'partner': 0, 'is_engaged': False} for j in range(n)]

# first occurring index is a woman
for i in range(0, len(arr), n+1):
    temp_arr = arr[i:i+n+1]
    index = temp_arr[0] - 1

    # Determine if woman or man
    if not women[index]['preferences']:
        # for women store inverted array
        w_pref = [0 for x in range(n)]
        for j in range(1, n+1):
            w_pref[temp_arr[j] - 1] = j - 1

        women[index]['preferences'] = w_pref
    else:
        # for men store array as normal

        men[index]['preferences'] = [x - 1 for x in temp_arr[1:]]


print('Reading time: ', time.time() - t1)
t2 = time.time()
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


sys.stdout.write('\n'.join(str(women[i]['partner'] + 1) for i in range(n)))
sys.stdout.write('\n')

print('Solving time: ', time.time() - t2)
