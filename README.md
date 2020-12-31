# -tic.toe-and-board-game
# in this we created a tic.toe.py game for two individual player 
# one tic.toe.bot.py for single player

# Example for tic.toe.py for two players.
:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
#this box is the position box . input the given value to #enter the position of player=  to fill the given box......
# if you input 1 . the box[0][0][0]=x 
#similarly ....
# In this we use a numpy module . datatype array 

[Name of file=  tic.toe.py]

# This is a empty array......
[[['' '' '']
  ['' '' '']
  ['' '' '']]]
  
:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|  # this use to see the position of input.....
|[7 | 8 | 9]|
:-----------:

enter your position player1=1
[[['x' '' '']
  ['' '' '']
  ['' '' '']]]
*****************************

:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:


enter your position player2=2
[[['x' 'o' '']
  ['' '' '']
  ['' '' '']]]
*****************************
enter your position player1=4
[[['x' 'o' '']
  ['x' '' '']
  ['' '' '']]]
*****************************

:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:


enter your position player2=3
[[['x' 'o' 'o']
  ['x' '' '']
  ['' '' '']]]
 ****************************
enter your position player1=7
[[['x' 'o' 'o']
  ['x' '' '']
  ['x' '' '']]]
player1 won!



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Example of tic toe.bot.py for single player . player v/s bot
:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>

[Name of file=  tic.toe.bot.py]

bot input is = 4
[[['' '' '']
  ['x' '' '']
  ['' '' '']]]
*******************

:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
enter your position sir=1
[[['o' '' '']
  ['x' '' '']
  ['' '' '']]]
************************



bot input is = 6
[[['o' '' '']
  ['x' '' 'x']
  ['' '' '']]]
************************

:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
enter your position sir=2
[[['o' 'o' '']
  ['x' '' 'x']
  ['' '' '']]]
******************************

bot input is = 3
[[['o' 'o' 'x']
  ['x' '' 'x']
  ['' '' '']]]


:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
enter your position sir=7
[[['o' 'o' 'x']
  ['x' '' 'x']
  ['o' '' '']]]
***********************

bot input is = 5
[[['o' 'o' 'x']
  ['x' 'x' 'x']
  ['o' '' '']]]
Bot won!
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

one tic toe game is also created . In this you can see a different logic but same output ......
# In this we dictionary data type . to create a list and use to create tic.toe game....

[Name of file=  tic.toe-2.py]
T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


 | |
-+-+-
 | |
-+-+-
 | |
player onet1
*********



T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


X| |
-+-+-
 | |
-+-+-
 | |
player two=t2
*********



T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


X|O|
-+-+-
 | |
-+-+-
 | |
player one=m1
*********



T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


X|O|
-+-+-
X| |
-+-+-
 | |
player two=t3
*********



T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


X|O|O
-+-+-
X| |
-+-+-
 | |
player one=d1
*********



T1|T2|T3
- +- +-
M1|M2|M3
- +- +-
D1|D2|D3
*********


X|O|O
-+-+-
X| |
-+-+-
X| |
Player One Won!!
