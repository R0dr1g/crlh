def randintlist(len, ceiling):
    import random
    randomlist = list()

    for i in range(len):
        randomlist.append(random.randint(0, ceiling))

    return randomlist







try:
    print()
    print("How many numbers do you want to generate?")
    len = int(input())
    print()
    print("Limit :")
    ceiling = int(input())
    randintlist(len, ceiling)
except ValueError:
    print("Ain't a number nickel galium")
