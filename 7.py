def compare_strings(str1, str2):
    if str1 < str2:
        return f'The first string "{str1}" comes before the second string "{str2}".'
    elif str1 > str2:
        return f'The first string "{str1}" comes after the second string "{str2}".'
    else:
        return f'The first string "{str1}" is equal to the second string "{str2}".'
str1=input("Enter first string: ")
str2=input("Enter second string: ")
result = compare_strings(str1, str2)
print(result)