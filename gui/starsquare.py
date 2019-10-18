def starsquare(n):
    for i in range(n):
        str(i+1)
        star = ""
        print(star, "*", i+1)
        print("*", 1+1)


print("How many stars do you want on each side?")

try:
    n = int(input())
    starsquare(n)
except ValueError:
    print("Not a number!")
