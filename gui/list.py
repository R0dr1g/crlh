def printlist(mylist):
    formatted_content = ""
    counter = 1
    print()
    for elem in mylist:
        if(counter==1):
            formatted_content += elem
        elif(conter == len(mylist)):
            formatted_content += " and "+elem
        else:
            formatted_content +=", "+elem
        counter = counter + 1
    print(formatted_content)
    print()
