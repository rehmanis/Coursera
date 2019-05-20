# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [5, 5] # pixels per update (1/60 seconds)
paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
PAD_VEL = 4

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    
    ball_vel[0] = random.randrange(2, 4)
    ball_vel[1] = -random.randrange(1, 3)
    
    # change the horizontal velocity direction if the ball needs to be spawn in the LEFT direction
    if (direction == LEFT):
        ball_vel[0] = -ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    # reset the scores
    score1 = 0
    score2 = 0
    # spawn ball in random direction
    spawn_ball(random.randrange(LEFT,RIGHT+1)) 

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # determine whether paddle and ball collide  
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        # ball is touching or passed the left side of the canvas
        if ( ball_pos[1] - BALL_RADIUS >  paddle1_pos + PAD_HEIGHT or ball_pos[1] + BALL_RADIUS < paddle1_pos ):
            spawn_ball(RIGHT)
            score2 += 1
        else:
            ball_vel[0] = -1.1* ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
            
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        # ball is touching or passed the right side of the canvas
        if ( ball_pos[1] - BALL_RADIUS >  paddle2_pos + PAD_HEIGHT or ball_pos[1] + BALL_RADIUS < paddle2_pos ):
            spawn_ball(LEFT)
            score1 +=1
        else:
            ball_vel[0] = -1.1*ball_vel[0] 
            ball_vel[1] = 1.1*ball_vel[1]
            
    # reflect the ball when colliding with the top or bottom of the canvas    
    if (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    elif ( ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    # draw the scores so before ball so that it is behind the ball    
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT/8), 40, 'White')
    canvas.draw_text(str(score2), (WIDTH*3.0/4, HEIGHT/8), 40, 'White')        
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if (paddle1_pos < 0 ):
        paddle1_pos = 0
    elif (paddle1_pos > HEIGHT - PAD_HEIGHT):
        paddle1_pos = HEIGHT - PAD_HEIGHT
        
    if (paddle2_pos < 0 ):
        paddle2_pos = 0
    elif (paddle2_pos > HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT  
        
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],
                         [PAD_WIDTH,paddle1_pos + PAD_HEIGHT],
                         [0, paddle1_pos + PAD_HEIGHT]], 1, 'White', 'White')
    
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos],
                         [WIDTH, paddle2_pos + PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], 1, 'White', 'White')
              
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["down"]):
        paddle2_vel += PAD_VEL
        
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel -= PAD_VEL

    if (key == simplegui.KEY_MAP["s"]):
        paddle1_vel += PAD_VEL
        
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_vel -= PAD_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
        
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel = 0
        
    if (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
        
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
restartButton = frame.add_button('restart', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
