import  numpy as np 
import random 

random_no=random.randint(1,7)
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
step=0
path=np.array(a,dtype=np.int64)
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
print(path)
# l for left and r for right and d for down and u for up
user_code=input('''Enter you code:\n''').replace(' ','').lower().strip()
if len(user_code)==0:
    print('None.....')
    print(exit())
 # l2-d3-l3
check_format=user_code.count('l')+user_code.count('d')+user_code.count('r')+user_code.count('u')+user_code.count('i')+user_code.count('s')
if user_code.count('-')== check_format-1:
    pass
else:
    print('Invalid format: command-command-commnad-so on ')
    print(exit())
code=list(user_code.split('-'))

direction=['l','d','r','u','i','s']
flag=False
for i in range(len(code)):
    if code[i][0] in direction:
        pass
    else:
        print(f'Invalid Command:({code[i]},{code[i][0]})')
        bool=True
if bool == True:
    print(exit())       

    
def find_user():
    for i in range(len(path)):
        for j in range(len(path[0])):
            if path[i][j]==1:
                return i,j
            
wrong_command=[]
for command in code:
    try:                              
        if command[0] == 'l':
            row=find_user()[0]
            colum=find_user()[1]
            if path[row][colum+(int(command[1])-1)] == 0:
                path[row][colum] = 0
                path[row][colum+(int(command[1])-1)] = 1
            else:
                wrong_command.append(command)
        elif command[0] == 'd':
            row=find_user()[0]
            colum=find_user()[1]
            if path[row+(int(command[1])-1)] [colum] ==0:
                path[row][colum] = 0
                path[row+(int(command[1])-1)] [colum] = 1
            else:
                wrong_command.append(command)
        elif command[0] == 'r':
            row=find_user()[0]
            colum=find_user()[1]
            if path[row][colum-(int(command[1])-1)]==0:
                path[row][colum] = 0
                path[row][colum-(int(command[1])-1)]= 1
            else:
                wrong_command.append(command)
        elif command[0] == 'u':
            row=find_user()[0]
            colum=find_user()[1]
            if path[row-(int(command[1])-1)] [colum] == 0:
                path[row][colum] = 0
                path[row-(int(command[1])-1)] [colum] = 1
            else:
                wrong_command.append(command)
        elif command[0]=='s':
            if len(command)==3 or len(command)==4 or len(command)==5:
                swap_position=list(command[1:len(command)].split(','))
                
                for i in range(len(swap_position)):
                    if swap_position[i]. isnumeric() ==True:
                        swap_position[i]=int(swap_position[i])
                    else:
                        print(f'Invalid command in {command}:{swap_position[i]}')
                        break
                def get_row_colum(index):
                    if swap_position[index]>=1 and swap_position[index]<=len(path[0]):
                        return 0,int(swap_position[index])-1
                    elif swap_position[index]>=len(path[0])+1 and swap_position[index]<=len(path[0])*2:
                        return 1,(int(swap_position[index])-6)-1
                    elif swap_position[index]>=(len(path[0])*2)+1 and swap_position[index]<=len(path[0])*3:
                        return 2,(int(swap_position[index])-12)-1
                    elif swap_position[index]>=(len(path[0])*3)+1 and swap_position[index]<=len(path[0])*4:
                        return 3,(int(swap_position[index])-18)-1
                    else:
                        return 0,0
                row_1,colum_1=get_row_colum(0)
                row_2,colum_2=get_row_colum(1)
                row=find_user()[0]
                colum=find_user()[1]
                if row_1== row and colum_1==colum or row_2== row or colum_2==colum:
                    print(f'Invalid swap position {swap_position[0]}:{swap_position[1]}')
                    break
                else:
                    path[row_1][colum_1],path[row_2][colum_2]=path[row_2][colum_2],path[row_1][colum_2]
                    
        elif command[0]=='i':
            if len(command)==2:
                if command[1]=='x':
                    path=np.flip(path,axis=1)
                elif command[1]=='y':
                    path=np.flip(path,axis=0)
                else:
                    print(f'Invlaid axis{command}:',command[1])
                    break
            else:
                print(f'Invalid Command lenght {command}:{len(command)}?{2}')
                break
        print('=========================')
        step=step+1
        print(f'Step:{step}')
        print(path)
    except Exception as e:
        print(e)
        print(f'Problem in command:{command}')
        print("Error.. . Bug in the code...")    
         
         
if len(wrong_command)!=0:
    for error in wrong_command:
        print(f'Problem in command: {error}')
print('\n')

print('Complete Exceution Of Command Result:')
print(path)

if path[len(path)-1][0]==1 or path[len(path)-1][len(path[0])-1]==1:
    print(f'Congratulation you done it :{user_code}')
