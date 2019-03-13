#https://codeforces.com/contest/1130/problem/B

n = int(input())
a = list(map(int, input().split()))

x = [-1 for i in range(n + 1)]
y = [-1 for i in range(n + 1)]

for i in range(2 * n):
    if x[a[i]] == -1:
        x[a[i]] = i
    else:
        y[a[i]] = i

ans = x[1] + y[1]

for i in range(1, n):
    ans += min(abs(x[i] - x[i + 1]) + abs(y[i] - y[i + 1]), abs(x[i] - y[i + 1]) + abs(y[i] - x[i + 1]))

print(ans)
