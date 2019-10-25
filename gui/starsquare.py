def starsquare(n):
    for i in range(n):
        print("*")
    star = ""
    for i in range(n):
        star += "*"
    return star


print("How many stars do you want on each side?")

try:
    n = int(input())
    print()
    print(starsquare(n))

except ValueError:
    print("Not a number!")
