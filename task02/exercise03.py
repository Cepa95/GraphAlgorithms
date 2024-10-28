def countAdjacentVowels(checkString):
    counter = 0
    vowels = "AEIOUaeiou"
    for i in range(len(checkString) - 1):
        if checkString[i] in vowels and checkString[i + 1] in vowels:
            counter += 1
    return counter


checkString = "JAAAabuKaaa"

print(countAdjacentVowels(checkString))
