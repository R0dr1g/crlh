
def randmult(number, ceiling):
    import random
    randquest = ""
    for i in range(number):
        a = str(random.randint(0, ceiling))
        b = str(random.randint(0, ceiling))
        randquest = a + " x " + b
    return randquest



try:
    print()
    print("How many mults do you want to generate?")
    number = int(input())
    print()
    print("Limit :")
    ceiling = int(input())
    print(randmult(number, ceiling))
except ValueError:
    print("Not a number !")
