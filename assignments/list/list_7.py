# 문제 7.

# 10개의 정수를 입력받아 리스트에 저장한 후 짝수 번째 입력된 값의 합과 홀수 번째 입력된 값의 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수첫째자리까지 출력한다.
# 입력 예: 95 100 88 65 76 89 58 93 77 99
# 출력 예:
# sum : 446
# avg : 78.8

num_list = []
even_list = []
odd_list = []
i = 1
for i in range(10) :
    num = int(input("정수를 입력하세요 : "))
    num_list.append(num)
    if  i % 2 == 0 :
        odd_list.append(num)
    else :
        even_list.append(num)

result_even = sum(even_list)
result_odd = sum(odd_list) / 5

print("sum : {}\navg : {}".format(result_even,result_odd))