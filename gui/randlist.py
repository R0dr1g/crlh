def randintlist(len, ceiling):
    list1 = [randint()]


print()
print("How many numbers do you want to generate??")
len = input()
print()
print("Limit :")
print()
ceiling = input()

try:
    len = int(input())
    ceiling = int(input())
    randintlist(len, ceiling)
except ValueError:
    print("Ain't a number nickel galium")
