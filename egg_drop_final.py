from sense_hat import SenseHat
###Egg Drop###
###Coded by dan_aldred###

import time
import random
sense = SenseHat()
sense.clear()

global game_over
global score

game_over = False
basket_x = 7
score =  0

'''main pitch measurement'''
def basket_move(pitch, basket_x):
    sense.set_pixel(basket_x, 7, [0, 0, 0])
    new_x = basket_x
    if 1 < pitch < 179 and basket_x != 0:
        new_x -= 1
    elif 359 > pitch > 179 and basket_x != 7:
        new_x += 1
    return new_x,

'''Main game setup'''
def main():
    global game_over
        
    '''Introduction'''
    sense.show_message("Egg Drop", text_colour = [255, 255, 0])
    sense.set_rotation(90)
    sense.load_image("chick.png")
    time.sleep(2)
    sense.set_rotation()

    '''countdown'''
    countdown = [3, 2, 1]
    for i in countdown:
        sense.show_message(str(i), text_colour = [255, 255, 255])
        
    basket_x = 7
    egg_x = random.randrange(0,7)
    egg_y = 0
    sense.set_pixel(egg_x, egg_y, [255, 255, 0])
    sense.set_pixel(basket_x, 7, [139, 69, 19])
    time.sleep(1)
       
    while game_over == False:
        global score
        '''move basket  first'''
        '''Get basket position'''
        pitch = sense.get_orientation()['pitch']
        basket_x, = basket_move(pitch, basket_x)
        
        '''Set Basket Positon'''
        sense.set_pixel(basket_x, 7, [139, 69, 19])
        time.sleep(0.2)
         
        '''Egg drop'''
        sense.set_pixel(basket_x, 7, [0, 0, 0])
        sense.set_pixel(egg_x, egg_y, [0, 0, 0])
        egg_y = egg_y + 1
        #print (egg_y)
        sense.set_pixel(egg_x, egg_y, [255, 255, 0])

        '''Check posiion of the egg and basket x , y'''
        if (egg_y == 7) and (basket_x == egg_x or basket_x-1 == egg_x ):
            sense.show_message("1up", text_colour = [0, 255, 0])
            sense.set_pixel(egg_x, egg_y, [0, 0, 0])#hides old egg
            egg_x = random.randrange(0,7)
            score = score =+ 1
            egg_y = 0
            
        elif egg_y == 7:
            sense.show_message("Game Over", text_colour = [255, 38, 0])
            return score
            game_over = True
            break
        
main()
time.sleep(1)
sense.clear()
sense.show_message("You Scored " + str(score), text_colour = [128, 45, 255], scroll_speed = 0.08)



