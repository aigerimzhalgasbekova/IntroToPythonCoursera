# template for "Stopwatch: The Game"
import simplegui

# define global variables
position = [50, 50]
width = 300
height = 300
time = 0
A=0
B=0
C=0
D=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A,B,C,D
    m = str(t)
    if (0<=t<=9):
        A=0
        B=0
        C=0
        D = t
    elif (10<=t<=99):
        A=0
        B=0
        C = int(m[0])
        D = int(m[1])
    elif (100<= t <= 599):
        A=0
        B = int(m[0])
        C = int(m[1])
        D = int(m[2])
    elif (t>=600):
        A = t//600
        n = str(t%600)
        
        if (0<=int(n)<=9):
            B = 0
            C = 0
            D = int(n)
       
        elif (10<=int(n)<=99):
            B = 0
            C = int(n[0])
            D = int(n[1])
           
        elif (100<= int(n) <= 599):
            B = int(n[0])
            C = int(n[1])
            D = int(n[2])
           
    else:
        print 'Error'
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    timer.stop()
    global time
    time = 0

# define event handler for timer with 0.1 sec interval

def tick():
    global time
    time += 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 36, 'White')
    
# create frame
f = simplegui.create_frame('Stopwatch', width, height)

# register event handlers
timer = simplegui.create_timer(100, tick)
f.add_button('Start', start, 50)
f.add_button('Stop', stop, 50)
f.add_button('Reset', reset, 50)
f.set_draw_handler(draw)

# start frame
f.start()
