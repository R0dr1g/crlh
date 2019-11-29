try:
    print()
    print("Number of questions :")
    number = int(input())
    print()
    print("Ceiling :")
    ceiling = int(input())
    print()
    yyy = list()
    for i in range(number):
        def randmult(a, b):
            randquest = ("How much is " + str(a) + " / " + str(b) + "?")
            yyy.append(randquest)
            return randquest
    answer = list()
    correction = list()
    for q in range(number):
        import random
        a = int((random.randint(0, ceiling)))
        b = int((random.randint(0, ceiling)))
        print(randmult(a, b))
        answer.append(int(input()))
        correction.append(a/b)
    counter = 0
    def coransw(a, b):
        correct = ("Q" + str(i+1) + ") " + str(yyy[i]) + " User answered " + str(answer[i]) + ". The answer was correct!")
        return correct
    def wrongans(a, b):
        wrong = ("Q" + str(i+1) + ") " + str(yyy[i]) + " User answered " + str(answer[i]) + ". The answer was wrong.")
        return wrong
    print()
    for i in range(number):
        if (answer[i] == correction[i]):
            print(coransw(a, b))
            counter +=1
        if (answer[i] != correction[i]):
            print(wrongans(a, b))

    def score():
        zzz = (str(counter) + " out of " + str(number))
        return zzz
    print()
    print(score())
except ValueError:
    print("Not a number !")
