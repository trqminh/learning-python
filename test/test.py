n, m = list(map(int, input().split(' ')))

mat = [None for i in range(n)]

for i in range(n):
    mat[i] = list(map(int, input().split(' ')))


tmp_xor = 0
for i in range(n):
    tmp_xor ^= mat[i][0]


if tmp_xor:
    print('TAK')
    for i in range(n):
        print('1 ', end = '')
else:
    flag = False
    idx = 0
    val = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] != mat[i][0]:
                flag = True
                idx = i
                val = j
                break

        if flag:
            break

    if flag:
        print('TAK')
        for i in range(idx):
            print('1', end = ' ')

        print(val+1, end = ' ')

        for i in range(idx+1, n, 1):
            print('1', end = ' ')
    else:
        print('NIE')

