def check(str1, str2):
    result=str1+str2
    try:
        result=int(result)
        print("All Digits converted: ", result)
    except:
        print("String: ", result)
str1=input("Enter first string: ")
str2=input("Enter second string: ")
check(str1, str2)