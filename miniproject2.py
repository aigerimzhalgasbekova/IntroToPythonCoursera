import simplegui
import random
import math

secret_number = 0
i = 0
x=100
y=0
low = y
high = x
d = high - low + 1
n = int(math.ceil(math.log(d, 2)))

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global x
    global y
    if x:
        print 'Range ' + str(y) + ' ' + str(x)
        secret_number = random.randrange (y, x)
        return secret_number
    else:
        return

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global x
    x = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global x
    x = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global g
    g = int(guess)
    print 'Guess was ' + guess
    global secret_number
    if (g==secret_number):
        print 'Correct!'
        new_game()
    elif (g < secret_number):
        print 'The number is higher'
    else:
        print 'The number is lower'
    global n
    n = n - 1
    print 'Number of remaining guesses is '+ str(n)
    
    if (n == 0):
        print 'You lose! \n Game over!'
        new_game()

    
# create frame
f = simplegui.create_frame('GuessNumber', 300, 300)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 100)
f.add_button('Range is [0, 1000)', range1000, 100)
f.add_input('Guess', input_guess, 100)


# call new_game 
new_game()
f.start()
