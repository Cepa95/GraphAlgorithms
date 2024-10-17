def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def nthPrime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
    return num


n = 2
print(nthPrime(n))
