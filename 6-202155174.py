from cs1robots import *
load_world("C:/Users/julia/Anaconda3/Lib/worlds/rain1.wld")
hubo=Robot(beepers=10,orientation="E", avenue=2, street=6)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

hubo.move()
hubo.turn_left()
for i in range(4):
    while hubo.front_is_clear():
        hubo.move()
        if hubo.left_is_clear():
            hubo.drop_beeper()
    turn_right()

count = 0
while not hubo.left_is_clear():
    count+=1
    hubo.move()
hubo.turn_left()

if count == 1:
    while hubo.front_is_clear():
        hubo.move()
        if hubo.left_is_clear():
            hubo.drop_beeper()
    turn_right()
    while not hubo.left_is_clear():
        hubo.move()
    hubo.turn_left()