def newFunc():
    print("Function Example")
    print("함수를 쓸때는 들여쓰기를 한다.")

def FoundFunc():
    newFunc()
    newFunc()

FoundFunc()

for i in range (4):
    print("반복문 4번")
print("반복하지 않는 이유: 들여쓰기를 하지 않아 반복하지 않음")