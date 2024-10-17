def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def sumOfPrimes(evenNumber):
    if evenNumber % 2 != 0:
        return

    pairs = []
    for i in range(2, (evenNumber // 2) + 1):
        if isPrime(i) and isPrime(evenNumber - i):
            pairs.append((i, evenNumber - i))

    return pairs


evenNumber = 30
print(sumOfPrimes(evenNumber))
