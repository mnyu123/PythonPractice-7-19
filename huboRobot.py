from cs1robots import * # 강의자료에 있는 라이브러리임

create_world() # 맵 생성

hubo = Robot(beepers = 1) # 로봇 생성

hubo.move() # 로봇 움직임
hubo.move()
hubo.move()

hubo.turn_left() # 로봇 좌회전

hubo.move()


def turn_right(): # 로봇 우회전 
        hubo.turn_left() # 좌회전을 3번 하면 우회전을 1번 한것과 같음
#turn_right()


def turn_around():
    hubo.turn_left()
    hubo.turn_left()
#turn_around()

def climb_up_four_stairs():
    for i in range(4):
        climb_up_one_stairs()
climb_up_four_stairs()

def climb_up_one_stairs():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()