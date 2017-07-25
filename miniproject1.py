import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        return 'There is no such value!'

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        return 'rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        return 'You should choose number in the range from 0 to 4!'
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print '\n'
    
    # print a blank line to separate consecutive games
    print 'Player chooses ' + player_choice

    # print out the message for the player's choice
    player_number = name_to_number(player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0, 4)

    # compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)

    # convert comp_number to comp_choice using the function number_to_name()
    print 'Computer chooses ' + comp_choice
    # print out the message for computer's choice
    diff = (comp_number - player_number)%5
    
    if diff==1 or diff==2:
        print 'Computer wins!'
    elif diff==3 or diff==4:
        print 'Player wins!'
    else:
        print 'Try again!’

# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()
