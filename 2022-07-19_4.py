# while 반복문
# 조건이 참이라면 명령 계속 수행

# 휴보 미로 탈출 (if , while 사용)
# 1. 시작점에 비퍼놓기
# 2. 벽을 만날때 까지 전진
# 3. 좌회전 하기
# 4. 2,3번 과정을 거치면서 비퍼를 발견할때 까지 반복
# 5. 비퍼를 발견할시 종료


from cs1robots import *

create_world()

hubo = Robot(beepers = 1) # 로봇 생성

# 1. 시작점에 비퍼놓기
hubo.drop_beeper()
while not hubo.front_is_clear(): # 휴보앞에가 막혀있다면
    hubo.turn_left() # 계속 좌회전하라
hubo.move()
# 2. 벽을 만날때 까지 전진
while not hubo.on_beeper(): # 휴보가 시작위치에 왔는지 검사
    if hubo.right_is_clear():
        turn_right()
        hubo.move() 
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left() # 앞이 막히면 좌회전
# 이후 반복

# 좋은 코드 작성 원칙
## 1. 사람이 이해할만한 코멘트 붙이기
## 2. 코드에 의미있는 이름 붙이기
## 3. 프로그램은 TOP-DOWN으로 진행한다

# 1. 간단히 시작하자.
# 2. 한번에 하나의 작은 작업만 수행시키기
# 3. 각각의 작업이 이전 작업에 영향을 주지 않기 (보수적으로 프로그램 개선)
# 4. 알기쉬운 주석 달기
# 5. 의미를 잘 전달하는 아름 고르기