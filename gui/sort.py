try:
    import random
    print()
    print("How many numbers u want?")
    lenght = int(input())
    print()
    print("Maximum :")
    ceiling =  int(input())
    sortlist = list()
    for i in range(lenght):
        sortlist.append(random.randint(0, ceiling))
    print()
    print("Original list: " + str(sortlist))
    print()
    def sortint():
        sortlist.sort()
        return sortlist
    print("Here is the list sorted in ascending order: " + str(sortint()))
except ValueError:
    print("Not an integer!")
