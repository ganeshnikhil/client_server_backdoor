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
[[['' '' '']
  ['' '' '']
  ['' '' '']]]
enter your position player1=1
[[['x' '' '']
  ['' '' '']
  ['' '' '']]]


:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:


enter your position player2=2
[[['x' 'o' '']
  ['' '' '']
  ['' '' '']]]
enter your position player1=4
[[['x' 'o' '']
  ['x' '' '']
  ['' '' '']]]


:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:


enter your position player2=3
[[['x' 'o' 'o']
  ['x' '' '']
  ['' '' '']]]
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


bot input is = 4
[[['' '' '']
  ['x' '' '']
  ['' '' '']]]


:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
enter your position sir=1
[[['o' '' '']
  ['x' '' '']
  ['' '' '']]]




bot input is = 6
[[['o' '' '']
  ['x' '' 'x']
  ['' '' '']]]


:-----------:
|[1 | 2 | 3]|
|[4 | 5 | 6]|
|[7 | 8 | 9]|
:-----------:
enter your position sir=2
[[['o' 'o' '']
  ['x' '' 'x']
  ['' '' '']]]


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


bot input is = 5
[[['o' 'o' 'x']
  ['x' 'x' 'x']
  ['o' '' '']]]
Bot won!
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# you should enter position in imput box and the box will fill.

# one board game is also added to make fun the game .
[[0 0 0 0 0 0 1 0 0 0]
 [0 0 0 0 0 2 0 0 0 0]]
enter position=1
[[0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 2 0 0 0 0]]
enter position=2
[[0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 2 0 0 0]]
enter position=1
[[0 0 0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 2 0 0 0]]
enter position=2
[[0 0 0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 2 0 0]]
enter position=-1
[[0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 2 0 0]]
enter position=0
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0]]
player 1 win the game!
game done!
you can see here how game work .
1 will move one move forward in colum[0]
-1 will move one move backward in colum[0]
2 will move one move forward in colum[1]
-2 will move one move backward on columm[1]
0 will move downward 1 . means from colum[0] to colum[1]
-0 will move upward 2 .means from colum[1] to colum[0]
. these are the all input that you can enter in the input box .

# for more detail you can see code .....
