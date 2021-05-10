from cs1robots import *
load_world("C:/Users/julia/Anaconda3/Lib/worlds/trash4.wld")
hubo=Robot()
hubo.set_trace("blue")

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

number=0
while True :
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()
    if not hubo.front_is_clear():
        number+=1
        if number%2==1:
            hubo.turn_left()
            if not hubo.front_is_clear() and not hubo.right_is_clear():
                break
            hubo.move()
            hubo.turn_left()
        elif number%2==0:
            turn_right()
            if not hubo.front_is_clear() and not hubo.left_is_clear():
                break
            hubo.move()
            turn_right()

while not hubo.facing_north():
    hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()

hubo.turn_left()
while hubo.carries_beepers():
    hubo.drop_beeper()