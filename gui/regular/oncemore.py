def gui(message, number):
    print()
    for i in range(number):
        str(i+1)
        print(message)
    print()

finish = False
while finish == False:
    print()
    print("diz gui crlh")
    message = input()
    print("diz um numero crlh")
    try:
        number = int(input())
        gui(message, number)
    except ValueError:
        print("Isso n é numero crlho")

    g = input("Queres continuar crlh (ye/nah nigga)")
    if (g != "ye"):
        finish = True
