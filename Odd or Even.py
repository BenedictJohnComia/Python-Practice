# %%
#Odd or Even Tester
testNum = int(input("Enter a number to be evaluated: "))
if testNum % 2 != 0:
    print(testNum, "is an odd number")
else:
    print(testNum, "is an even number")

# %%
#The following codeblock involves input from the user and lists.
def inputList(inputNum):
    cntr = 0
    sampleList = []
    if cntr < inputNum:
        for x in range(inputNum):
            num = int(input("Enter a number to be included in the list"))
            sampleList.append(num)
    
    print("The list created is", sampleList)
    return sampleList

inputNum = int(input("Enter the number of items to be included in the list: "))

completeList = inputList(inputNum)

for x in completeList:
    if x % 2 == 0:
        print(x, "is an even number")
    else:
        print(x, "is an odd number")




