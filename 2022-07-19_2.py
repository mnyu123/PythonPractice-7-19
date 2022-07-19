from cs1robots import *

create_world()

hubo = Robot(beepers = 1) # 로봇 생성

def move_or_trun():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

for i in range(35):
    move_or_trun()