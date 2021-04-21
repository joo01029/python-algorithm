
def getPrimeNumber(x):
    a = [False, False] + [True] * (x - 1)
    primes = []
    for i in range(2, x-1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, x-1, i):
                a[j] = False;
    return primes

print(getPrimeNumber(10))