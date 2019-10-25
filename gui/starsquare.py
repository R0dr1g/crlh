def starsquare(n):
    star = ""
    for k in range(n):

        for i in range(n):

            star += "*"
        star += "\n"
    return star


print("How many stars do you want on each side?")

try:
    n = int(input())
    print(starsquare(n))

except ValueError:
    print("Not a number!")
