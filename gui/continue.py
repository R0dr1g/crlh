finish = False
while finish == False:
    print ("Do you want to continue ?? (Yes/No)")

    m = input()

    if (m !="Yes"):
        finish = False
    if(m !="No"):
        finish = True
    else:
        print("I don't understand you, sorry!")
