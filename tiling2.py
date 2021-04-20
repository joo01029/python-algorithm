dp = [0 for i in range(1001)]

def tilling(t):
    if t == 0:
        return 1
    if t == 1:
        return 0
    if t == 2:
        return 3
    result = 3*tillin(t-2)
    for i in range(3,t+1):
        if i % 2 == 0:
            result += 2* tiling(x - i)
    dp[x] = result
