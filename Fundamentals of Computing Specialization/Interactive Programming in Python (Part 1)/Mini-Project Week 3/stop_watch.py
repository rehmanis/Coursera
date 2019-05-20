import simplegui

# define global variables
countTenthOfSec = 0
successStops = 0
totStops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #get the tenth of the second digit
    D = t % 10
    #get the total seconds
    t = t / 10
    #convert seconds to minutes
    A = t/60
    #store the remaining seconds after converting to minutes
    BC = t % 60
    #get the unit digit of the seconds
    C = BC % 10
    #get the tens digit of the seconds
    B = (BC - C)/10
    
    return (str(A) + ":" + str(B) + str(C) + "." + str(D))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    timer.start()
    
def stop_button_handler():
    global totStops, successStops
    if (timer.is_running()):
        timer.stop()
        totStops += 1
        if (not(countTenthOfSec % 10)):
            successStops +=1

def reset_button_handler():
    global countTenthOfSec, totStops, successStops
    timer.stop()
    countTenthOfSec = 0
    totStops = 0
    successStops = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global countTenthOfSec
    countTenthOfSec += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(countTenthOfSec), (100, 175), 50, 'White')
    canvas.draw_text(str(successStops) + "/" + str(totStops), (250,50), 30, 'White')

# create frame
frame = simplegui.create_frame("Stop Watch", 300,300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
startButton = frame.add_button('start', start_button_handler, 100)
stopButton = frame.add_button('stop', stop_button_handler, 100)
resetButton = frame.add_button('reset', reset_button_handler,100)

# start frame
frame.start()
timer.start()