try:
    import math
    print("Greatest common diviser between :")
    a = int(input())
    print()
    print("And : ")
    b = int(input())
    print()
    def mygcd(a, b):
        return math.gcd(a, b)
    print("GCD of " + str(a) + " and " + str(b) + " is " + str(mygcd(a, b)) + ".")
except ValueError:
    print("Not an int..")
