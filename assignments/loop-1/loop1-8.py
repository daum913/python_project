# 문제 8.(for)

# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.
# 입력 예: 10 15
# 출력 예: sum : 37 avg : 12.3
num_1 = int(input("첫 번째 정수를 입력하세요 : "))
num_2 = int(input("두 번째 정수를 입력하세요 : "))
list = []
sum = 0
if num_1 > num_2 :
    for i in range(num_2, num_1+1) :
        if i % 3 == 0 or i % 5 == 0 :
          sum += i
          list.append(i)
elif num_1 < num_2 :
    for i in range(num_1, num_2+1) :
        if i % 3 == 0 or i % 5 == 0 :
          sum += i
          list.append(i)
print("sum : {}, avg : {}".format(sum,round(sum/len(list),1)))