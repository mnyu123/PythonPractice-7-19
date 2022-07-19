from cs1robots import *

create_world()

hubo = Robot(beepers = 1) # 로봇 생성

def move_and_pick():
    hubo.move()
    if hubo.on_beeper(): # 휴보가 있는자리에 비퍼가 있으면
        hubo.pick_beeper() # 비퍼를 주워라
        # 비퍼가 없다면 수행하지 않음
move_and_pick()
# 조건문의 값 , True / False

# 현재 위치에 비퍼가 없을때 비퍼를 떨어트리기
if not hubo.on_beeper(): # not 조건을 반대로 함
    hubo.drop_beeper()

for i in range(9):
    move_and_pick()