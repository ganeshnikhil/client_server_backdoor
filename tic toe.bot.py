import numpy as np
import pyttsx3
import random
import time
block = 0

print(":-----------:")
print("|[1 | 2 | 3]|")
print("|[4 | 5 | 6]|")
print("|[7 | 8 | 9]|")
print(":-----------:")


# here we try to create a input for bot . x will genrate input from 0 to 8 , so we add 1 on all to make it 1 to 9
# bot logic to play move!.....
bot = []
x = random.sample(range(9), 9)
for i in range(len(x)):
    y = x[i]+1
    bot .append(y)
# print(bot)


speaker = pyttsx3.init()
speaker.setProperty('rate', 130)    # Speed percent (can go over 100)
speaker.setProperty('volume', 0.9)  # Volume 0-1
speaker.say("please don't repeat your input!")
speaker.say("hi sir thanks for  the chance to play with you ")
speaker.say("let's start the game now  ")
speaker.runAndWait()


a = np.zeros((1, 3, 3), dtype=str)
check_list = []
# print(a)
print("\n")


print("*************************************************************************")  # >
for i in range(8):  # >
    p1 = bot[i]  # >
    check_list.append(p1)  # >
    Tuple = set(check_list)  # >
    time.sleep(2)  # >
# to put 'x' where bot input will tell.
    if p1 == 1:
        a[0][0][0] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 2:
        a[0][0][1] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 3:
        a[0][0][2] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 4:
        a[0][1][0] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 5:
        a[0][1][1] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 6:
        print("\n")
        a[0][1][2] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 7:
        a[0][2][0] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 8:
        a[0][2][1] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    elif p1 == 9:
        a[0][2][2] = 'x'
        print("\n")
        print("bot input is =", p1)
        print(a)

    else:
        print("\n invalid input")
        break
    # to check bot input . when bot won we exit() the game
    # to check verticaly and horizontaly
    # --------------------
    # |   *   |    *   |  *   |
    #  --------------------
    # |   *   |         |       |
    # --------------------
    # |   *   |         |       |'''
    # ---------------------
    if a[0][0][0] == 'x' and a[0][0][1] == 'x' and a[0][0][2] == 'x':
        print("Bot won!")
        print("*****************************************************************")
        print(exit())
    elif a[0][0][0] == 'x' and a[0][1][0] == 'x' and a[0][2][0] == 'x':
        print("Bot won!")
        print("*******************************************************************")
        print(exit())
    # to check verticaly and horizontaly
    # --------------------
    # |       |    *    |       |
    #  --------------------
    # |   *  |    *    |  *   |
    # --------------------
    # |       |    *    |       |'''
    # --------------------
    elif a[0][1][0] == 'x' and a[0][1][1] == 'x' and a[0][1][2] == 'x':
        print("Bot won!")
        print("*********************************************************************")
        print(exit())
    elif a[0][0][1] == 'x' and a[0][1][1] == 'x' and a[0][2][1] == 'x':
        print("bot won!")
        print("**********************************************************************")
        print(exit())
    # to check verticaly and horizontaly
    # -------------------
    # |       |        |   *   |
    # -------------------
    # |       |        |   *   |
    # -------------------
    # |   *  |  *    |   *   |'''
    # -------------------
    elif a[0][2][0] == 'x' and a[0][2][1] == 'x' and a[0][2][2] == 'x':
        print("Bot won!")
        print("********************************************************************")
        print(exit())
    elif a[0][0][2] == 'x' and a[0][1][2] == 'x' and a[0][2][2] == 'x':
        print("Bot won!")
        print("**********************************************************************")
        print(exit())
    # to check digonaly on board
    # ------------------
    # |    * |        |   *  |
    # -------------------
    # |       |   *   |       |
    # -------------------
    # |   *  |        |   *  |'''
    # -------------------
    elif a[0][0][0] == 'x' and a[0][1][1] == 'x' and a[0][2][2] == 'x':
        print("Bot won!")
        print("*******************************************************************")
        print(exit())
    elif a[0][0][2] == 'x' and a[0][1][1] == 'x' and a[0][2][0] == 'x':
        print("Bot won!")
        print("********************************************************************")
        print(exit())

    print("\n")
    print(":-----------:")
    print("|[1 | 2 | 3]|")
    print("|[4 | 5 | 6]|")
    print("|[7 | 8 | 9]|")
    print(":-----------:")
    # this part of code is used to check if no any result is found and whole box is filled
    block = block+1
    if block == 9:
        print("oops Draw!")
        print(exit())
    # it take input from player .
    p2 = int(input("enter your position sir="))

    # to avoid repeation we remove those input bot which player already chossen.
    for i in bot:
        if i == p2:
            bot.remove(i)
    # print(bot)
    check_list.append(p2)
    Tuple = set(check_list)
    # to put player input 'o' where player want .
    if p2 == 1:
        a[0][0][0] = 'o'
        print(a)
    elif p2 == 2:
        a[0][0][1] = 'o'
        print(a)
    elif p2 == 3:
        a[0][0][2] = 'o'
        print(a)
    elif p2 == 4:
        a[0][1][0] = 'o'
        print(a)
    elif p2 == 5:
        a[0][1][1] = 'o'
        print(a)
    elif p2 == 6:
        a[0][1][2] = 'o'
        print(a)
    elif p2 == 7:
        a[0][2][0] = 'o'
        print(a)
    elif p2 == 8:
        a[0][2][1] = 'o'
        print(a)
    elif p2 == 9:
        a[0][2][2] = 'o'
        print(a)
    else:
        print("\ninvalid input!")
        print("restart the game!")
        break

    # if input repeat then this part of code will excute .
    if len(check_list) != len(Tuple):
        print("invalid input")
        print(exit())
    # to check player input . when player won we exit() the game
    # to check verticaly and horizontaly
    # --------------------
    # |   *   |    *   |  *   |
    #  --------------------
    # |   *   |         |       |
    # --------------------
    # |   *   |         |       |
    # ---------------------
    if a[0][0][0] == 'o' and a[0][0][1] == 'o' and a[0][0][2] == 'o':
        print("you won!")
        print("*********************************************************************")
        print(exit())
    elif a[0][0][0] == 'o' and a[0][1][0] == 'o' and a[0][2][0] == 'o':
        print("you won!")
        print("*********************************************************************")
        print(exit())
    # to check verticaly and horizontaly
    # --------------------
    # |       |    *    |       |
    #  --------------------
    # |   *  |    *    |  *   |
    # --------------------
    # |       |    *    |       |'''
    # --------------------
    elif a[0][1][0] == 'o' and a[0][1][1] == 'o' and a[0][1][2] == 'o':
        print("you won!")
        print("********************************************************************")
        print(exit())
    elif a[0][0][1] == 'o' and a[0][1][1] == 'o' and a[0][2][1] == 'o':
        print("you won!")
        print("********************************************************************")
        print(exit())
    # to check verticaly and horizontaly
    # -------------------
    # |       |        |   *   |
    # -------------------
    # |       |        |   *   |
    # -------------------
    # |   *  |  *    |   *   |'''
    # -------------------
    elif a[0][2][0] == 'o' and a[0][2][1] == 'o' and a[0][2][2] == 'o':
        print("you won!")
        print("********************************************************************")
        print(exit())
    elif a[0][0][2] == 'o' and a[0][1][2] == 'o' and a[0][2][2] == 'o':
        print("you won!")
        print("**********************************************************************")
        print(exit())
    # to check digonaly on board
    # ------------------
    # |    * |        |   *  |
    # -------------------
    # |       |   *   |       |
    # -------------------
    # |   *  |        |   *  |
    # -------------------
    elif a[0][0][0] == 'o' and a[0][1][1] == 'o' and a[0][2][2] == 'o':
        print("you won!")
        print("************************************************************************")
        print(exit())
    elif a[0][0][2] == 'o' and a[0][1][1] == 'o' and a[0][2][0] == 'o':
        print("you won!")
        print("*************************************************************************")
        print(exit())
    block = block+1
    # this part of code is used to check if no any result is found and whole box is filled
    if block == 9:
        print("oops Draw!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
