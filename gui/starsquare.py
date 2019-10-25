def starsquare(n):
    for i in range(n):
    star = ""
    for i in range(n):
        star += "*"
    return star n times


print("How many stars do you want on each side?")

try:
    n = int(input())
    print()
    print(starsquare(n))

except ValueError:
    print("Not a number!")
