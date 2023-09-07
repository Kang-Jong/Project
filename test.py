import random
radom_number = random.randint(1,100)

while True:
    try:
        answer = int(input('정답이라고 생각하는 숫자를 적어주세요:'))
        if answer == radom_number:
            print("정답입니다.")
            break
        elif answer > radom_number:
            print("정답이 해당 숫자보다 작습니다.")
        elif answer < radom_number:
            print("정답이 해당 숫자보다 큽니다.")
    except:
        print("1~100까지의 숫자를 입력해주세요.")
