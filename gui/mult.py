
def randmult(a, b):
    randquest = (a + " x " + b)
    return randquest



try:
    import random
    print()
    print("How many mults do you want to generate?")
    number = input()
    print()
    print("Limit :")
    ceiling = int(input())
    print()

    for q in number:
        a = int(str(random.randint(0, ceiling)))
        b = int(str(random.randint(0, ceiling)))
        print(randmult(a, b))
        answer = list()
        answer.append(int(input()))
        correction = list()
        correction.append(a*b)

except ValueError:
    print("Not a number !")
