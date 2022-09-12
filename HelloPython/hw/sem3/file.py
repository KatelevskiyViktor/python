# ex1:
# import random
# 
# sumValue = 0
# myList = []
# for i in range(1, 6):
#     myList.append(random.randrange(1, 6))
# 
# for i in range(1, len(myList)):
#     if i % 2 != 0:
#         sumValue += myList[i]
# 
# print("Your List is: " + str(myList))
# print("Sum: " + str(sumValue))


# ex2:
# 
# arrOne = [2, 3, 4, 5, 6]
# arrTwo = [2, 3, 5, 6]
# 
# def composition(arr):
#     tempStart = 0
#     tempEnd = len(arr)-1
#     res = []
#     while True:
#         if tempStart == tempEnd:
#             res.append(arr[tempStart]**2)
#             break
#         elif tempStart > tempEnd:
#             break
# 
#         res.append(arr[tempStart] * arr[tempEnd])
#         tempStart += 1
#         tempEnd -= 1
#     print()
#     print('Your list before: ' + str(arr))
#     print('Multiplication list is: ' + str(res))
#     print()
# 
# composition(arrOne) 
# composition(arrTwo)   


# ex3:
# 
# myList = [1.1, 1.2, 3.1, 10.01]
# tempList = []
# 
# for fNum in myList:
#     tempStr = str(fNum)
#     tempStrList = tempStr.split('.')
#     tempList.append(float('1.' + tempStrList[1]))
# 
# print(round(max(tempList) - min(tempList), 2))


# ex4:
# 
# print(format(45, 'b'))
# print(format(3, 'b'))
# print(format(2, 'b'))

# ex5:
from audioop import reverse


listFibEnd = []
listFibStart = []
fib1 = fib2 = 1
n = 8
i = 0

while i < n:
    if(i < 2):
        listFibStart.append(i)
        if(i == 1):listFibStart.append(i)
        i += 1
        continue
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    listFibStart.append(fib2)
    i += 1
    
listFibEnd = listFibStart.copy()
listFibStart.reverse()

for i in range(0, len(listFibStart)):
    if i%2 == 0:
        listFibStart[i] = -listFibStart[i]

print(listFibStart[:-1] + listFibEnd )