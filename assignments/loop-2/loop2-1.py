# 문제 1.

# 1부터 100까지의 정수 중 한 개를 입력받아 100 보다 작은 배수들을 차례로 출력하다가 10 의 배수가 출력되면 프로그램을 종료하도록 프로그램을 작성하시오.
# 입력 예: 7
# 출력 예: 7 14 21 28 35 42 49 56 63 70


num = int(input("1부터 100까지의 정수를 입력하세요 : "))
i = 1
while  i < 10 :
    print(num*i)
    i += 1
    if (num * i) > 100 :
        break
    elif (num * i) % 10 == 0:
        print(num * i)
        break
   