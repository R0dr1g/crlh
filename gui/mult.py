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
    answer = list()
    correction = list()
    for q in range(number):
        import random
        a = int((random.randint(0, ceiling)))
        b = int((random.randint(0, ceiling)))
        print(randmult(a, b))
        answer.append(int(input()))
        correction.append(a*b)

    def corasnw():
        correct = ("Q" + str(i+1) + ") " + str(a) + " x " + str(b) + " User answered " + str(answer[i]) + ". The answer was correct!")
        return correct
    def wrongans():
        wrong = ("Q" + str(i+1) + ") " + randmult(a, b) + " User answered " + str(answer[i]) + ". The answer was wrong.")
        return wrong
    print()
    for i in range(number):
        if (answer == correction):
            print(coransw())
        if (answer != correction):
            print(wrongans())
except ValueError:
    print("Not a number !")
