import math
import random
x_vals = list()
print("f(x) = sin(x), x = ")
x_vals.append(int(input()))
def func(x):
    return (math.sin(x))

for x in x_vals:
    print("x : " + str(x))
    try:
        print("f(" + str(x) + ") = " + str(func(x)))
    except ZeroDivisionError:
        print("Can't divide by 0 bruh")
