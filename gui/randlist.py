def randintlist(len, ceiling):
    print()
    for i in range(len):
        str(i+1)
        print randint(len, ceiling)

print()
print("Number of potential numbers :")

len = input()

print()
print("The maximum potential number :")

ceiling = input()

try:
    len = int(input())
    ceiling = int(input())
    randintlist(len, ceiling)
except ValueError:
    print("Ain't a number nickel galium")
