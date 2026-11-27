# cook your dish here
t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    print((x // 10) * n)