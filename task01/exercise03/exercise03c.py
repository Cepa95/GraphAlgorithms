def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def findTwinPrimes(n):
    twinPrimes = []
    previousPrime = None

    for num in range(2, n + 1):
        if isPrime(num):
            if previousPrime is not None and num - previousPrime == 2:
                twinPrimes.append((previousPrime, num))
            previousPrime = num

    return twinPrimes


n = 10
print(findTwinPrimes(n))
