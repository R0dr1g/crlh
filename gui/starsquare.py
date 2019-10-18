def starsquare(n):
    for i in range(n):
        str(i+1)
        star = ""
        print(star, "* ")
        print()
        print("* ")


print("How many stars do you want on each side?")

try:
    n = int(input())
    starsquare(n)
except ValueError:
    print("Not a number!")
