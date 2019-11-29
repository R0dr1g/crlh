list1 = ["Gui", "Gil", "Francisco", "Filipe", "David"]
print()

print("Full List :")
print(list1)
print()

print("First Element :")
print(list1[0])
print()

print("Last Element :")
print(list1[-1])
print()

counter = 1

for elem in list1:
    print(str(counter), ": ", elem)

    counter = counter + 1
