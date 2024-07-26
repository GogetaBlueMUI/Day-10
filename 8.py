def string_transforms(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()}
str=input("Enter string: ")
result = string_transforms(str)
print(result)