import random
print()
print("Ceiling : ")
ceiling = int(input())
print("Number of integers :")
number = int(input())
randlist = list()
for i in range(number):
    randlist.append(random.randint(0, ceiling))
print("original list :" + str(randlist))
def sortlist():
    randlist.sort()
    return randlist
print("ascending order" + str(sortlist()))
