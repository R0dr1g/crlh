def repeat_message(message, number):
    print()
    for i in range(number):
        print(str(i+1), message)
    print()

print()
print("Message :")
message = input()
print()
print("Number of times you want to repeat the message :")
try:
    number = int()
    print()
    repeat_message(message, number)
except ValueError:
    print("Ain't a number nigga")
