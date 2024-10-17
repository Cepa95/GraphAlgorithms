def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):  # zbog 4
        if num % i == 0:
            return False
    # print(num, end=" ")
    return True


def countPrime(a, b):
    if a > b:
        a, b = b, a

    start = int(a)
    end = int(b)

    counter = 0
    for num in range(start, end + 1):
        if isPrime(num):
            counter += 1

    return counter


a = 2
b = 20
print(countPrime(a, b))
