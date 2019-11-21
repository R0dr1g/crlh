try:
    print()
    print("Number of questions :")
    number = int(input())
    print()
    print("Ceiling :")
    ceiling = int(input())
    print()
    def randmult(a, b):
        randquest = ("How much is " + str(a) + " x " + str(b) + "?")
        return randquest

    for q in range(number):
        import random
        a = int((random.randint(0, ceiling)))
        b = int((random.randint(0, ceiling)))
        print(randmult(a, b))
        answer = list()
        answer.append(int(input()))
        correction = list()
        correction.append(a*b)

    def allansw(a, b, c)):
        for i in range(c):
            correct = ("Q" + str(i+1))
except ValueError:
    print("Not a number !")
