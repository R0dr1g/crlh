
def randmult(number, ceiling):
    import random
    randquest = list()
    for i in range(number):
        a = str(random.randint(0, ceiling))
        b = str(random.randint(0, ceiling))
        randquest.append(a + " x " + b)
    return randquest




try:
    print()
    print("How many mults do you want to generate?")
    number = int(input())
    print()
    print("Limit :")
    ceiling = int(input())
    print()
    randquest = randmult(number, ceiling)
    for q in randquest:

        print(q)
        answer = list()
        answer.append(int(input()))
    gui = randmult(number, ceiling)
    for a in randquest:
        correction = list()
        correction.append(a*b)

except ValueError:
    print("Not a number !")
