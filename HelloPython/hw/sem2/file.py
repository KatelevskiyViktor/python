import random
# ex1:
# print('Enter number: ')
# st = input()
# num = 0
# 
# st = list(st)
# 
# for x in st:
#     print(x)
#     if x == ',':
#         continue
#     num += int(x)
# 
# print('Sum your number is: ' + str(num))


# ex2:
# print('Enter num:')
# num = int(input())
# myList = []
# temp = 1
# 
# for i in range(1, num + 1):
#     for y in range(1, i + 1):
#         temp *= y
#     myList.append(temp)
#     temp = 1
# 
# print(myList)


# ex3:
# print('Enter number: ')
# n = int(input())
# sum = 0
# 
# for i in range(1, n + 1):
#     sum += ((1 + (1/i)) ** i)
# 
# print('Sum is: ' + str(sum))


# ex4:
# from random import randrange
# 
# print('Enter number: ')
# n = int(input())
# print('Enter string indexes, format(1, 5, 3): ')
# s = input()
# sList = s.split(', ')
# 
# myList = []
# composition = 1
# 
# for i in range(1, n + 1):
#     myList.append(random.randrange(-n, n))
# 
# for i in sList:
#     composition *= myList[int(i)]
# 
# print("Your random list: " + str(myList))
# print("Composition is: " + str(composition))



# ex5:
# print('Enter number: ')
# n = int(input())
# myList = []
# 
# for i in range(1, n + 1):
#     myList.append(i)
# 
# print("Your list befor shuffle: " + str(myList))
# random.shuffle(myList)
# print("Your list after shuffle: " + str(myList))
