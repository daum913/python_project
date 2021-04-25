# 문제 7.(for)

# 100 이하의 두 개의 정수를 입력받아 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예: 5 10
# 출력 예: 5 6 7 8 9 10

num_1 = int(input("첫 번째 정수를 입력하세요 : "))
num_2 = int(input("두 번째 정수를 입력하세요 : "))
if num_1 > num_2 :
    for i in range(num_2, num_1+1) :
        print(i)
elif num_1 < num_2 :
    for i in range(num_1, num_2+1) :
        print(i)