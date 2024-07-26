def sizecheck(start, end, length):
    if start<0:
        print("Error!!")
    if end>length-1:
        print("Error!!")
def output(start, end, str):
    print("Sliced part: ", str[start:end])
str=input("Enter string: ")
start=int(input("Enter starting point: "))
end=int(input("Enter ending point: "))
length=len(str)
sizecheck(start, end, length)
output(start, end, str)