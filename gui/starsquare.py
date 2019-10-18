def starsquare(n):
    star = ""
    for i in range(n):
        star += "* "
        print("*")
    return star


print("How many stars do you want on each side?")
print()
try:
    n = int(input())
    print(starsquare(n))
except ValueError:
    print("Not a number!")
