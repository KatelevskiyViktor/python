from cgi import print_environ
from cmath import sqrt
from functools import cache
import math

# ex1:
# while True:
#     print('Enter number or q(if you want to exit):')
#     try:
#         val = input()
#         if val == 'q':
#             break
#         else:
#             val = int(val)
#     except ValueError:
#         print('This is not a number! Try again')
#         continue
# 
# 
#     if val > 0 and val < 8:
#         print(str(val) + ' -> yes')
#     else:
#         print(str(val) + ' -> no')


# ex2:
# for x in 0,1:
#    for y in 0,1: 
#         for z in 0,1:
#             left = not (x or y or z)
#             right = not x and not y and not z
#             print(f'not ({x} or {y} or {z}) == not {x} and not {y} and not {z} = ' + str(left == right))


# ex3:
# while True:
#     print("Enter x:")
#     x = int(input())
#     print("Enter y:")
#     y = int(input())
# 
#     if x == 0 or y == 0:
#         print('Enter not a zero')
#         continue
# 
#     if x > 0 and y > 0:
#         print("Quarter your point 1")
#     elif x > 0 and y < 0:
#         print("Quarter your point 2")
#     elif x < 0 and y < 0:
#         print("Quarter your point 3")
#     elif x < 0 and y > 0:
#         print("Quarter your point 4")
# 
#     break



# ex4:
# print('Enter number quarter:')
# x = int(input())
# if x == 1:
#     print('Value X is from 1 to +∞ and value Y is from 1 to +∞')
# elif x == 2:
#     print('Value X is from 1 to +∞ and value Y is from -1 to -∞')
# elif x == 3:
#     print('Value X is from -1 to -∞ and value Y is from -1 to -∞')
# elif x == 4:
#     print('Value X is from -1 to -∞ and value Y is from 1 to +∞')


# ex5:
print('Enter X point A:')
xA = int(input())
print('Enter Y point A:')
yA = int(input())
print('Enter X point B:')
xB = int(input())
print('Enter Y point B:')
yB = int(input())

distance = sqrt(((xB - xA) ** 2) + ((yB - yA) ** 2))
distance = round(distance.real, 3)
print("Distance from A to B is: " + str(distance)[:-1])