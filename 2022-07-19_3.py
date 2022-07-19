from cs1robots import *
import time

create_world()

hubo = Robot(beepers = 1) # 로봇 생성

def dance():
    for i in range(4):
        hubo.turn_left() # 시계 반대방향으로 한바퀴 돌기
        #time.sleep(500)

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        hubo.move()
        #time.sleep(500)
    else: # 전진하지 못할때 비퍼를 떨어트리는 조건
    # 조건 작성할때 들여쓰기 유의
        hubo.turn_left()
        hubo.drop_beeper()
        #time.sleep(500)

for i in range(18):
    move_or_turn()
    #time.sleep(500)

# 들여쓰기가 많은 조건문일때
# if / elif  <- else+if를 합친내용 두줄로 작성할것을 한줄로 요약한 것