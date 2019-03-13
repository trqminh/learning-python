# https://codeforces.com/contest/1117/problem/A

#TLE
n = int(input())
a = list(map(int, input().split()))

cnt = 0
ans = 0
for i in range(n):
    if a[i] == max(a):
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)
