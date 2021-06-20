import  numpy as np 
import random 
# import numpy and random module 
#  genrate random no between 1 to 7 
# according to random no path is choosen 
# if 1 then a elif 2 then .....
random_no=random.randint(1,8)
if random_no==1:
    a=[[1,0,0,2,2,2],[2,2,0,0,0,2],[2,2,2,2,0,0]]
elif random_no==2:
    a=[[0,1,0,2,2,2],[2,2,0,0,2,2],[2,2,2,0,0,0]]
elif random_no==3:
    a=[[0,2,1,2,2,2],[2,2,0,2,2,2],[2,2,0,0,0,0]]
elif random_no==4:
    a=[[2,2,2,2,1,0],[2,2,2,0,0,0],[0,0,0,0,2,2]]
elif random_no==5:
    a=[[1,2,2,2,2,2],[0,0,0,2,2,2],[2,2,0,0,0,0]]
elif random_no== 6:
    a=[[1,2,0,0,0,2],[0,2,0,2,0,2],[0,0,0,2,0,0]]
elif random_no== 7:
    a=[[1,2,0,0,0,0],[0,0,0,2,0,0],[0,0,0,0,0,2]]
elif random_no==8:
    #l3-s2,4-l2-d2-l2-d4-s30,3-l2
    a=[[1,0,0,2,2,2],[2,2,2,0,0,2],[2,0,2,2,0,2],[0,0,0,0,0,2],[2,2,2,2,0,2]]
# intialize a variable  step use furthure in code.
step=0
# convert 2-d path into 2-d path array
path=np.array(a,dtype=np.int64)
# comment for help uset to understand the format 
print('"l" for [left][p] and"r" for [right][p] and "d" for [down][p] and "u" for [up][p] and "s" for [swap][p1],[p2] and "i" for inverse [inverse][axis]')
print('|||||||||||||||||||||||||||||||||||||||||||||||||||READ|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('================================================================================================================')
print('''
[left][postion] ex:[1,0,0,0,0] :[l][5] means left 5 :l for left and 5 for p =[0,0,0,0,1]
[right] [postion] ex:[0,0,0,0,1]:[r][5] means right 5: r for right and 5 for p =[1,0,0,0,0]
[down] [position] ex:[[2,2,1],[2,2,0]] :[d][2] means down 2 : d for down and 2 for p =[[2,2,0],[2,2,1]]
[up] [position] ex:[[2,2,0],[2,2,1]]: [u][2] means up 2 : u for up and 2 for p =[[2,2,1],[2,2,0]]
[swap][postion1][postion2] ex:[[1,2,0],[2,0,0]]: [s][1],[4]  means swap 1 to 4 =[[2,2,0],[1,0,0]] 
[inverse][axis] ex:[[1,2,0],[2,0,0]] :[i][x] means inverse along x =[[0, 2, 1],[0, 0, 2]] 
[inverse][axis] ex:[[1,2,0],[2,0,0]]: [i][y] means inverse along y =[[2, 0, 0],[1, 2, 0]]
[format to write]first command-second command- third command - .....so on : ex: l4-r2-d3-s2,6-iy.............so on
''')
print('===============================================================================================================')
# print the path 
print(path)
# l for left and r for right and d for down and u for up
# Take inpu from user . replace(),lower(),strip() functions are used to modify user input . remove unwanted spaces and  lower the alphabet 
user_code=input('''Enter you code:\n''').replace(' ','').lower().strip()
# if user input nothing ..means len(user_code)==0 then exit() the program.
if len(user_code)==0:
    print('None.....')
    print(exit())
 # l2-d3-l3
# to check the format of user_code so we count all possible command left,down,right,up,inverse,swap and add them 
check_format=user_code.count('l')+user_code.count('d')+user_code.count('r')+user_code.count('u')+user_code.count('i')+user_code.count('s')
# compare the with the count of '-' format :ls-u3-d2-s3,5
# we know the '-' will 1 less than the check foramt variable.
# if this is true then right foramt 
if user_code.count('-')== check_format-1:
    pass
# else wrong exit()
else:
    print('Invalid format: command-command-commnad-so on ')
    print(exit())
 # we take user string input into list so we split user input from '-' and put into the list code.
code=list(user_code.split('-'))
# these are possible valid commands l,d,r,u,i,s put it into a list direction 
direction=['l','d','r','u','i','s']
# intiliaze a flag to false
flag=False
# loop on the code list and check it is valid direction from direction list 
for i in range(len(code)):
    # if it's true then pass
    if code[i][0] in direction:
        pass
    # else print the all error 
    else:
        print(f'Invalid Command:({code[i]},{code[i][0]})')
        # iniliaze flag -- true
        flag=True
 # it means a invalid command so we exit()
if flag == True:
    print(exit())       

# then define a function find_user() our user is '1' it will return the position of '1' or user from the 2-d array   
def find_user():
    for i in range(len(path)):
        for j in range(len(path[0])):
            if path[i][j]==1:
                return i,j
# intialize a empty list to get all wrong command by user
wrong_command=[]
# loop on code list 
for command in code:
    # use try and except block for handling unexcepted errors
    try:
        # if our command[0] is l means left 
        if command[0] == 'l':
            # then we call the function to find user and get postion of row and colum of it 
            row=find_user()[0] # row of user in 2-d array
            colum=find_user()[1] # colum of user in 2-d array 
            # name of 2-d array is path 
            # check if path is valid according to user input: 0 means vlaid 
            if path[row][colum+(int(command[1])-1)] == 0:
                # then the postion of user is  empty : means 0
                path[row][colum] = 0
                # we move user left to the given input postion
                path[row][colum+(int(command[1])-1)] = 1
            else:
                # else append the wrong command
                wrong_command.append(command)
        # elif our command[0] is d means downn 
        elif command[0] == 'd':
             #then we call the function to find user and get postion of row and colum of it 
            row=find_user()[0] # row of user in 2-d array
            colum=find_user()[1] # olum of user in 2-d array 
            # check if path is valid according to user input 0 means valid 
            if path[row+(int(command[1])-1)] [colum] ==0:
                # then the potion of user is empty :means 0
                path[row][colum] = 0
                # then we move user down to the given input postion 
                path[row+(int(command[1])-1)] [colum] = 1
            else:
                # else append the wrong command 
                wrong_command.append(command)
         # elif our command[0] is r means right 
        elif command[0] == 'r':
            # then we call the fucntions to find user and get postion of row and colum of it 
            row=find_user()[0] # row of userr in 2-d array
            colum=find_user()[1] # colum of user in 2-d array
            # check if path is valid according to user input if 0 means valid 
            if path[row][colum-(int(command[1])-1)]==0:
                # then the postion of user is empty means 0
                path[row][colum] = 0
                # then we move user down to the given unput postion 
                path[row][colum-(int(command[1])-1)]= 1
            else:
                # else append the wrong command 
                wrong_command.append(command)
         # similarly u means up 
        elif command[0] == 'u':
            row=find_user()[0]
            colum=find_user()[1]
            if path[row-(int(command[1])-1)] [colum] == 0:
                path[row][colum] = 0
                path[row-(int(command[1])-1)] [colum] = 1
            else:
                wrong_command.append(command)
         # s means swap 
        elif command[0]=='s':
            # if lenght of command is start with three and max lenght 5 : s17,16 . s2,5 . s12,2 . if valid then 
            if len(command)==4 or len(command)==5 or len(command)==6:
                # remove teh s from command [1: len(command)]then split the command by ',' and put into the list swap_postions 
                swap_position=list(command[1:len(command)].split(','))
                # loop through the swap_postion list and check if value is numeric if true then convert into int 
                for i in range(len(swap_position)):
                    if swap_position[i]. isnumeric() ==True:
                        swap_position[i]=int(swap_position[i])
                    # exit() the loop and print the error 
                    else:
                        print(f'Invalid command in {command}:{swap_position[i]}')
                        break
                        # define a fuction to get the row and colum of user input user input format is 
                        # [s] [p1] [p2] p1 in 1 to 18 format means 17,18 or 7,9 or so on not in index foramt 
                        # convert numeric format into index foramt 
                        # ex s1,10 index foramt s[0][0],[1][2]
                 # pass the index of swap_postion as parameter 
                def get_row_colum(index):
                    # if input is between 1 to len(path[0]) means it is 0th row 
                    # 6(row)+colum=swap_postion[index]
                    # now we know the row find the colum=(int(swap_position[index])-6)-1
                    # similarly find all 
                    # fucntion return the row and colum
                    if swap_position[index]>=1 and swap_position[index]<=len(path[0]):
                        return 0,int(swap_position[index])-1
                    elif swap_position[index]>=len(path[0])+1 and swap_position[index]<=len(path[0])*2:
                        return 1,(int(swap_position[index])-6)-1
                    elif swap_position[index]>=(len(path[0])*2)+1 and swap_position[index]<=len(path[0])*3:
                        return 2,(int(swap_position[index])-12)-1
                    elif swap_position[index]>=(len(path[0])*3)+1 and swap_position[index]<=len(path[0])*4:
                        return 3,(int(swap_position[index])-18)-1
                    elif swap_position[index]>=(len(path[0])*4)+1 and swap_position[index]<=len(path[0])*5:
                        return 4,(int(swap_position[index])-24)-1
                    elif swap_position[index]>=(len(path[0])*5)+1 and swap_position[index]<=len(path[0])*6:
                        return 5,(int(swap_position[index])-30)-1
                    else:
                        return 0,0
                # pass the index and get the row ans colum postion for swap 
                row_1,colum_1=get_row_colum(0)
                row_2,colum_2=get_row_colum(1)
                # we have to check the user dosen't swap user with the end directly.
                row=find_user()[0]
                colum=find_user()[1]
                # check the condition for it 
                if row_1== row and colum_1==colum or row_2== row and colum_2==colum:
                    print(f'Invalid swap position {swap_position[0]}:{swap_position[1]}')
                    break
                # swap the postions 
                else:
                    path[row_1][colum_1],path[row_2][colum_2]=path[row_2][colum_2],path[row_1][colum_1]
            else:
                print(f'Invalid command lenght {len(command)}')
                break
         # elif command[0] is i means inverse       
        elif command[0]=='i':
             # flip the the 2-d path array along the axis givnen by user 
              # check the length of command is 2
            if len(command)==2:
                # if x the flip along x
                if command[1]=='x':
                    path=np.flip(path,axis=1)
                 # elif along y 
                elif command[1]=='y':
                    path=np.flip(path,axis=0)
                  # else invlid format command 
                else:
                    print(f'Invlaid axis{command}:',command[1])
                    break
              # else len is not 2 then break out the loop 
            else:
                print(f'Invalid Command lenght {command}:{len(command)}?{2}')
                break
        print('=========================')
        # print step 
        step=step+1
        print(f'Step:{step}')
        # print otput of each command 
        print(path)
     # if exception ocuur print the exception
    except Exception as e:
        # print the exception....
        print(e)
        print(f'Problem in command:{command}')
        print("Error.. . Bug in the code...")    
         
 # len of wrong_command list is not 0 then print the wrong command 
if len(wrong_command)!=0:
    for error in wrong_command:
        print(f'Problem in command: {error}')
print('\n')
# print the complete exceution of command on path once
print('Complete Exceution Of Command Result:')
print(path)
# if the postion of user means '1' on these position it means you done it hurry ...
if path[len(path)-1][0]==1 or path[len(path)-1][len(path[0])-1]==1:
    print(f'Congratulation you done it :{user_code}')
else:
    print('Btter luck next time.....')
