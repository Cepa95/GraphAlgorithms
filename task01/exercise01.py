def isPythagoreanTriple(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

def getNumbers():
    while True:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = int(input("Enter the third number: "))
        
        if a <= 0 or b <= 0 or c <= 0:
            print("All numbers must be greater than 0")
            break
        
        print(isPythagoreanTriple(a, b, c))

getNumbers()