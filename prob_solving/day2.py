# https://codeforces.com/contest/1130/problem/C

import math

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n = int(input())
r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))

r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

vis = [[False for p in range(n)] for q in range(n)]

big_flag = False

grid = []

for i in range(n):
    tmp = str(input())
    grid.append(tmp)


def is_in_grid(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def dfs1(i, j, S):
    vis[i][j] = True

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if is_in_grid(ni, nj) and vis[ni][nj] == False and grid[ni][nj] == '0':
            S.append((ni, nj))
            if (ni == r2 and nj == c2):
                big_flag = True

            dfs1(ni, nj, S)


def dfs2(i, j, T):
    vis[i][j] = True

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if is_in_grid(ni, nj) and vis[ni][nj] == False and grid[ni][nj] == '0':
            T.append((ni, nj))
            dfs2(ni, nj, T)


def notEuclid(cell_1, cell_2):
    return int(math.pow(cell_1[0] - cell_2[0], 2) + math.pow(cell_1[1] - cell_2[1], 2))


def main():

    S = []
    S.append((r1, c1))
    dfs1(r1, c1, S)

    if (big_flag):
        print("0")
    else:
        T = []
        T.append((r2, c2))
        dfs2(r2, c2, T)

        ans = 1000000
        for i in range(len(S)):
            for j in range(len(T)):
                ans = min(ans, notEuclid(S[i], T[j]))

        print(ans)


if __name__ == '__main__':
    main()
