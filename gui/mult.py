
def randmult(number, ceiling):
    import random
    randomult = ""
    for i in range(number):
        a = str(random.randint(0, ceiling))
        b = str(random.randint(0, ceiling))
        randquest = a + " x " + b
    return randquest
    if


finish
while finish == False:
    try:
        print()
        print("How many mults do you want to generate?")
        number = int(input())
        print()
        print("Limit :")
        ceiling = int(input())
        randmult(number, ceiling)
    except ValueError:
        print("Not a number !")
