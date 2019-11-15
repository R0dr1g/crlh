
def randmult(a,b):
    import random
    randquest = (a + " x " + b)
    return randquest




try:
    print()
    print("How many mults do you want to generate?")
    number = int(input())
    print()
    print("Limit :")
    ceiling = int(input())
    print()
    randquest = randmult(a,b)

    for q in randquest:
        a = str(random.randint(0, ceiling))
        b = str(random.randint(0, ceiling))
        print(q)
        answer = list()
        answer.append(int(input()))
    gui = randmult(a,b)
    for a in gui:

        correction = list()
        correction.append(a*b)

except ValueError:
    print("Not a number !")
