import math
import random
x_vals = list()
print("f(x) = (3/2)*x, x = ")
x_vals.append(int(input()))
def func(x):
    return (3/2)*x

for x in x_vals:
    print("x : " + str(x))
    try:
        print("f(" + str(x) + ") = " + str(func(x)))
    except ZeroDivisionError:
        print("Can't divide by 0 bruh")
