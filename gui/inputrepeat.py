def repeat_message(message, number):
    print()
    for i in range(number):
        str(i+1)
        print(message)
    print()

print()
print("Message :")
message = input()
print()
print("Number of times you want to repeat the message :")
try:
    number = int(input())
    print()
    repeat_message(message, number)
    print()
except ValueError:
    print("Ain't a number")
