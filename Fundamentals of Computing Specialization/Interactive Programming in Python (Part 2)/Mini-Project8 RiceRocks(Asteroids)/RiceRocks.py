# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
ROTATE_STEP = 0.0873
COEFF_FRIC = 0.02
MAX_ROCK_ANG_VEL = 0.1
MIN_ROCK_ANG_VEL = -0.1
INIT_MAX_ROCK_VEL = 0.3
INIT_MIN_ROCK_VEL = -0.3
MAX_NUM_OF_ROCKS = 12
ACC = 0.2

max_rock_vel = INIT_MAX_ROCK_VEL
min_rock_vel = INIT_MIN_ROCK_VEL
score_to_change_vel = 5
vel_multiplier = 1
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# helper function to update and draw sprite in a group
def process_sprite_group(group_of_sprite, canvas):
    for sprite in set(group_of_sprite):
        sprite.draw(canvas)
        if (sprite.update()):
            group_of_sprite.remove(sprite)
                     
# helper function to check collision between a group of sprite and a single sprite        
def group_collide(group_of_sprite, other_object):
    # initialize the global variables
    global an_explosion_group
    
    collision = False
    for sprite in set(group_of_sprite):
        if sprite.collide(other_object):
            group_of_sprite.remove(sprite)
            an_explosion_group.add(Sprite(sprite.get_position(), sprite.get_velocity(), 
                                          sprite.get_angle(), 0, 
                                          explosion_image, explosion_info, explosion_sound))
            collision = True
            
    return collision

# helper function to check collisions between a group of sprite and other group of sprite
def group_group_collise(group_sprite, other_group_sprite):
    num_collisions = 0
    for sprite in set(group_sprite):
        if (group_collide(other_group_sprite, sprite)):
            group_sprite.remove(sprite)
            num_collisions += 1
    
    return num_collisions

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if (self.thrust):
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0],self.image_center[1]],
                              self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,
                              self.angle)
            
    def update(self):
        # position update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH 
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT 
        
        # add friction
        self.vel[0] *= (1 - COEFF_FRIC)
        self.vel[1] *= (1 - COEFF_FRIC)
        
        # update angular position
        self.angle += self.angle_vel
        
        # calculate the forward vector of the ship
        forward = angle_to_vector(self.angle)
        
        # update the velocity in the direction of forward vector
        if (self.thrust):
            self.vel[0] += ACC * forward[0]
            self.vel[1] += ACC * forward[1]
            
    def shoot_missile(self):
        global a_missile
        
        missile_pos = []
        missile_vel = []
        
        forward = angle_to_vector(self.angle)
        
        missile_pos.append(self.pos[0] + self.radius * forward[0])
        missile_pos.append(self.pos[1] + self.radius * forward[1])
        
        missile_vel.append(self.vel[0] + 6 * forward[0])
        missile_vel.append(self.vel[1] + 6 * forward[1])
        
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        a_missile_group.add(a_missile)

        
    def increment_angle_vel(self):
        self.angle_vel += ROTATE_STEP
    
    def decrement_angle_vel(self):
        self.angle_vel -= ROTATE_STEP
        
    def stop_rotation(self):
        self.angle_vel = 0
        
    def set_thrust(self, is_thrust_on):
        self.thrust = is_thrust_on
        
        if (is_thrust_on):
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
            
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if (self.animated):
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0] * self.age, self.image_center[1]], 
                              self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, 
                              self.image_size, self.angle)
    
    def update(self):
        
        # position update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH 
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT 
        
        # update angular position (for it to be rotating)
        self.angle += self.angle_vel
        
        # increment the age
        self.age += 1
        
        # check to see if the age of the sprite has exceeded its lifespan
        if (self.age < self.lifespan):
            return False
        else:
            return True
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def get_velocity(self):
        return self.vel
    
    def get_angle(self):
        return self.angle
    
    def get_angle_vel(self):
        return self.angle_vel
    
    def collide(self, other_object):
        if (dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius()):
            return True
        else:
            return False
        

           
def draw(canvas):
    global time, started, lives, score, a_rock_group, an_explosion, vel_multiplier
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw the score
    canvas.draw_text("Score: " +str(score), (WIDTH/10.0, HEIGHT/10.0), 30, 'white')
    canvas.draw_text("Lives: " +str(lives), (WIDTH * 8/10.0, HEIGHT/10.0), 30, 'white')
    
    
    # draw and update ships
    my_ship.draw(canvas)
    my_ship.update()
    
    # draw and update the group of sprite
    process_sprite_group(a_rock_group, canvas)
    process_sprite_group(a_missile_group, canvas)
    process_sprite_group(an_explosion_group, canvas)
           
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
    else:
        # check for collision between ship and rocks
        if group_collide(a_rock_group, my_ship):
            lives -= 1
            if (lives <= 0):
                started = False
                vel_multiplier = 1
                a_rock_group = set()
                timer.stop()
                soundtrack.rewind()
        
        # update the rock to missile collision and update the score  
        score += group_group_collise(a_missile_group, a_rock_group)

        
    
    
def keydown(key):
    if (key == simplegui.KEY_MAP["left"]):
        my_ship.stop_rotation()
        my_ship.decrement_angle_vel()
    elif (key == simplegui.KEY_MAP["right"]):
        my_ship.stop_rotation()
        my_ship.increment_angle_vel()
    elif (key == simplegui.KEY_MAP["up"]):
        my_ship.set_thrust(True)
    elif (key == simplegui.KEY_MAP["space"]):
        my_ship.shoot_missile()

def keyup(key): 
    if (key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]):
        my_ship.stop_rotation()
    elif (key == simplegui.KEY_MAP["up"]):
        my_ship.set_thrust(False)    
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn        
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        timer.start()
        soundtrack.play()

# timer handler that spawns a rock    
def rock_spawner():
    global a_rock_group, vel_multiplier, score_to_change_vel
    
    if (score >= score_to_change_vel):
        score_to_change_vel += 5
        vel_multiplier += 3
    
    if (len(a_rock_group) < MAX_NUM_OF_ROCKS):
        pos = []
        vel = []
        pos.append(random.randrange(0,WIDTH))
        pos.append(random.randrange(0, HEIGHT))
        vel.append(random.random() * ((max_rock_vel - min_rock_vel) + min_rock_vel)*vel_multiplier)
        vel.append(random.random() * ((max_rock_vel - min_rock_vel) + min_rock_vel)*vel_multiplier)
        ang = random.random() * (MAX_ROCK_ANG_VEL - MIN_ROCK_ANG_VEL) + MIN_ROCK_ANG_VEL
        
        a_rock = Sprite(pos, vel, 0, ang, asteroid_image, asteroid_info);
        if dist(a_rock.get_position(), my_ship.get_position()) > 1.5 * (a_rock.get_radius() + my_ship.get_radius()):
            a_rock_group.add(Sprite(pos, vel, 0, ang, asteroid_image, asteroid_info))
        
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], -1.57, ship_image, ship_info)
a_rock_group = set()
a_missile_group = set()
an_explosion_group = set()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()