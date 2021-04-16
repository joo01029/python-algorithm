d = [0 for i in range(0,1002)]

def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    if d[x != 0]:
        return d[x]
    d[x] = (dp(x-1) + dp(x-2)) %10007
    return d[x]

x= int(input())

print(dp(x))