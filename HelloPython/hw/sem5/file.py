# ex1:
# s = "Напишите программу, удаляющую из текстаабв все слова, содержащие \"абв\""
# import re
# s1 = re.sub("[а|б|в]","",s)
# s2 = re.sub("абв","", s)
# print (s1 + "\nВторой вариант: " + s2)


# ex2:
# from random import randint
# 
# def PlayWithMe():
#     while True:
#         print("Player №1, choice 'Heads'(enter 1) or 'Tails'(enter 0):")
#         playerOne = int(input())
#         playerTwo = 0
#         rand = randint(0, 1)
#         allCandy = 2021
        
#         if playerOne > 1 or playerOne < 0:
#             print("You are enter not validate number! Try again!")
#             continue

#         if playerOne == rand:
#             print("The first player walks first!")
#             mark = 0
#             while True:
#                 if mark == 0:
#                     print("The first player number: ")
#                     playerOne = int(input())
#                     if playerOne > 28 or playerOne < 1:
#                         print("Number need from 1 to 28! Please try again.")
#                         continue
#                     allCandy -= playerOne
#                     if allCandy <= 0:
#                         print("Player №1 WIN!!!!")
#                         break

#                 print("The second player number: ")
#                 playerTwo = int(input())
#                 if playerTwo > 28 or playerTwo < 1:
#                     print("Number need from 1 to 28! Please try again.")
#                     mark = 1
#                     continue
#                 mark = 0
#                 allCandy -= playerTwo
#                 if allCandy <= 0:
#                     print("Player №2 WIN!!!!")
#                     break
#                 print(f"Candy left:{allCandy}.")
#         else:
#             print("The second player walks first!")
#             mark = 0
#             while True:
#                 if mark == 0:
#                     print("The second player number: ")
#                     playerTwo = int(input())
#                     if playerTwo > 28 or playerTwo < 1:
#                         print("Number need from 1 to 28! Please try again.")
#                         continue
#                     allCandy -= playerTwo
#                     if allCandy <= 0:
#                         print("Player №2 WIN!!!!")
#                         break

#                 print("The first player number: ")
#                 playerOne = int(input())
#                 if playerOne > 28 or playerOne < 1:
#                     print("Number need from 1 to 28! Please try again.")
#                     mark = 1
#                     continue
#                 mark = 0
#                 allCandy -= playerOne
#                 if allCandy <= 0:
#                     print("Player №1 WIN!!!!")
#                     break
#                 print(f"Candy left:{allCandy}.")
#         break
# 
# def PlayWithComp():
#     while True:
#         print("Player, choice 'Heads'(enter 1) or 'Tails'(enter 0):")
#         playerOne = int(input())
#         playerTwo = 0
#         rand = randint(0, 1)
#         allCandy = 2021
#         tempAllCandy = 2021
        
#         if playerOne > 1 or playerOne < 0:
#             print("You are enter not validate number! Try again!")
#             continue

#         if playerOne == rand:
#             print("The player walks first!")
#             while True:
#                 print("The player number: ")
#                 playerOne = int(input())
#                 if playerOne > 28 or playerOne < 1:
#                     print("Number need from 1 to 28! Please try again.")
#                     continue
#                 allCandy -= playerOne
#                 if allCandy <= 0:
#                     print("Player WIN!!!!")
#                     break

#                 print("The computer number is: ")
#                 playerTwo = randint(1, 28)
#                 print(playerTwo)
#                 allCandy -= playerTwo
#                 if allCandy <= 0:
#                     print("Computer WIN!!!!")
#                     break
#                 print(f"Candy left:{allCandy}.")
#         else:
#             print("Computer walks first!")
#             mark = 0
#             first = 0
#             while True:
#                 if mark == 0:
#                     print("Computer number is: ")
#                     if first == 0:
#                         playerTwo = tempAllCandy % 29
#                         print(playerTwo)
#                         allCandy -= playerTwo
#                         first = 1
#                         continue
#                     playerTwo = randint(1, 28)
#                     allCandy -= playerTwo
#                     if allCandy <= 0:
#                         print("Computer WIN!!!!")
#                         break

#                 print("The player number: ")
#                 playerOne = int(input())
#                 if playerOne > 28 or playerOne < 1:
#                     print("Number need from 1 to 28! Please try again.")
#                     mark = 1
#                     continue
#                 mark = 0
#                 allCandy -= playerOne
#                 if allCandy <= 0:
#                     print("Player WIN!!!!")
#                     break
#                 print(f"Candy left:{allCandy}.")
#         break
# 
# print('You want play with computer(enter 1) or player (enter 0)?')
# selectGame = int(input())
# 
# if selectGame == 1:
#     PlayWithComp()
# else:
#     PlayWithMe()
    
    
# ex3:
# board = list(range(1,10))
# 
# def draw_board(board):
#     print ("-------------")
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-------------")
# 
# def take_input(player_token):
# 	valid = False
# 	while not valid:
# 		player_answer = int(input("Where will we put it " + player_token + "? "))
# 
# 		if player_answer >= 1 and player_answer <= 9:
# 			if (str(board[player_answer-1]) not in "XO"):
# 				board[player_answer-1] = player_token
# 				valid = True
# 			else:
# 				print ("This cell is already occupied")
# 		else:
# 			print ("Incorrect input. Enter a number from 1 to 9 to be like.")
# 
# def check_win(board):
# 	win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# 	for each in win_coord:
# 		if board[each[0]] == board[each[1]] == board[each[2]]:
# 			return board[each[0]]
# 	return False 
# 
# def main(board):
# 	counter = 0
# 	win = False
# 	while not win:
# 		draw_board(board)
# 		if counter % 2 == 0:
# 			take_input("X")
# 		else:
# 			take_input("O")
# 		counter += 1
# 		if counter > 4:
# 			tmp = check_win(board)
# 			if tmp:
# 				print (tmp, "Win!")
# 				win = True
# 				break
# 		if counter == 9:
# 			print ("Draw!")
# 			break
# 	draw_board(board)
# 
# main(board)


# ex4:
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Enter the text to be encoded: ")
print(f"Text after encoding: {coding(s)}")
print(f"Text after decryption: {decoding(coding(s))}")