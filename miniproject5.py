# implementation of card game - Memory

import simplegui
import random

cardlist = range(0, 8)*2

# helper function to initialize globals
def new_game():
    global state, turns, exposed, selected
    state = 0
    turns = 0
    random.shuffle(cardlist)
    print cardlist
    exposed=[False for n in cardlist] #for card_index in range(len(cardlist))]
    selected = []

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns
    index = pos[0]//50
    print index
    if not exposed[index]:
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if cardlist[selected[0]] != cardlist[selected[1]]:
                exposed[selected[0]]= exposed[selected[1]]=False
            selected.pop(1)
            selected.pop(0)
            state = 1
        selected.append(index)
        exposed[index] = True
    print state, exposed
    print selected
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #for i in range(16):
    for card_index in range(len(cardlist)):
        card_pos = 50*card_index
        if exposed[card_index]:
            canvas.draw_text(str(cardlist[card_index]), 
                         [card_pos+10, 70], 60, "White")
        else:
            canvas.draw_polygon([(card_pos, 0), (card_pos+50, 0), 
                             (card_pos+50, 100), (card_pos, 100),], 1, 
                            "Red", "Green")
    if all(exposed):
        canvas.draw_text("You win!", [350, 85], 36, "Red")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
