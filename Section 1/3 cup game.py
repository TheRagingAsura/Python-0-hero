
from random import shuffle

def shuffle_list(mylist):
  shuffle(mylist)
  return mylist



def player_guess():
  guess = ' '

  while guess not in ['0','1','2']:
    guess = input('Pick a number, 0,1 or 2')

  return int(guess)


def check_guess(mylist,guess):
  if mylist[guess] == 'O':
    print('Good Guess!')
  else:
    print('Wrong guess!!')
    print(mylist)





#Inital List
ball = [' ','0',' ']

#shuffle List 
ball_position = shuffle_list(ball)

#USER GUESS 
guess = player_guess()

#CHECK GUESS
check_guess(ball,guess)