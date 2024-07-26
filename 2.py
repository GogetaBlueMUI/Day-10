def indexx(str, index):
    length=len(str)
    if index>length-1:
        print("Error!!")
    else:
        print("Character: ", str[index])
str=input("Enter a string: ")
index=int(input("Enter the index number for the character: "))
indexx(str, index)