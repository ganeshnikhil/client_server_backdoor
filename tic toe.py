import numpy as np
import pyttsx3
count = 0

print(":-----------:")
print("|[1 | 2 | 3]|")
print("|[4 | 5 | 6]|")
print("|[7 | 8 | 9]|")
print(":-----------:")
print("\n")

# to give a voice interface this part of code is included ... for voice command
speaker = pyttsx3.init()
speaker.setProperty('rate', 130)    # Speed percent (can go over 100)
speaker.setProperty('volume', 1)  # Volume 0-1
speaker.say("please don't repeat your input!")
speaker.say("let's start the game now  ")
speaker.runAndWait()
# creating a empty array..
a = np.zeros((1, 3, 3), dtype=str)
check_list = []
print(a)
print('***********************************************************************************')
# it take input from user and add input at exact location on board game .. player1 can input his move  here ....
for i in range(8):
    p1 = int(input("enter your position player1="))
    check_list.append(p1)
    Tuple = set(check_list)
    if p1 == 1:
        a[0][0][0] = 'x'
        print(a)
    elif p1 == 2:
        a[0][0][1] = 'x'
        print(a)
    elif p1 == 3:
        a[0][0][2] = 'x'
        print(a)
    elif p1 == 4:
        a[0][1][0] = 'x'
        print(a)
    elif p1 == 5:
        a[0][1][1] = 'x'
        print(a)
    elif p1 == 6:
        a[0][1][2] = 'x'
        print(a)
    elif p1 == 7:
        a[0][2][0] = 'x'
        print(a)
    elif p1 == 8:
        a[0][2][1] = 'x'
        print(a)
    elif p1 == 9:
        a[0][2][2] = 'x'
        print(a)
    else:
        print("\ngame Draw!")
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
        print("player1 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][0] == 'x' and a[0][1][0] == 'x' and a[0][2][0] == 'x':
        print("player1 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
        print("player! won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][1] == 'x' and a[0][1][1] == 'x' and a[0][2][1] == 'x':
        print("player1won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
        print("player1won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][2] == 'x' and a[0][1][2] == 'x' and a[0][2][2] == 'x':
        print("player1won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
        print("player1 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][2] == 'x' and a[0][1][1] == 'x' and a[0][2][0] == 'x':
        print("player1won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())

    print("\n")
    print(":-----------:")
    print("|[1 | 2 | 3]|")
    print("|[4 | 5 | 6]|")
    print("|[7 | 8 | 9]|")
    print(":-----------:")
    print("\n")

    # this part of code is used to check if no any result is found and whole box is filled
    count = count+1
    if count == 9:
        print("Draw!")
        print(exit())

    p2 = int(input("enter your position player2="))
    check_list.append(p2)
    Tuple = set(check_list)

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
        print("\ngame Draw!")
        break


# if player repeat a input this part of code will  excute....
    if len(check_list) != len(Tuple):
        print("you may repeat your input!")
        print("invalid input")
        print(exit())

    # it check all row and colum for same input
    # to check player input . when player won we exit() the game
    # to check verticaly and horizontaly
    # --------------------
    # |   *   |    *   |  *   |
    #  --------------------
    # |   *   |         |       |
    # --------------------
    # |   *   |         |       |
    # ---------------------
    elif a[0][0][0] == 'o' and a[0][0][1] == 'o' and a[0][0][2] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][0] == 'o' and a[0][1][0] == 'o' and a[0][2][0] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][1] == 'o' and a[0][1][1] == 'o' and a[0][2][1] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][2] == 'o' and a[0][1][2] == 'o' and a[0][2][2] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())

    # to check digonaly on board.  /\/\/\/\/\/\....
    # ------------------
    # |    * |        |   *  |
    # -------------------
    # |       |   *   |       |
    # -------------------
    # |   *  |        |   *  |
    # -------------------
    elif a[0][0][0] == 'o' and a[0][1][1] == 'o' and a[0][2][2] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    elif a[0][0][2] == 'o' and a[0][1][1] == 'o' and a[0][2][0] == 'o':
        print("player2 won!")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(exit())
    # this part of code is used to check if no any result is found and whole box is filled
    count = count+1
    if count == 9:
        print("Draw!")
        print(exit())
