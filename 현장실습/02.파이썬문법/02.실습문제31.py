#실습문제 31
import random

#1~100 사이 랜덤한 값 생성
answer = random.randint(1,100)

try_count = 1
while True:
    x = int(input("(1~100) 숫자를 맞춰 보세요>>>"))
    
    if x > answer:
        print("down 입니다.")
    elif x < answer:
        print("up 입니다.")
    elif x == answer:
        print("정답입니다!")
        print("총시도횟수", try_count)
        break
    try_count += 1