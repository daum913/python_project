# 문제 1
# 다음 출력 예와 같이 출력되는 프로그램을 만드시오
# 합게와 평균은 수식을 이용한다
# 합계 : 세 과목 총합
# 평균 : 세 과목 평균
list = [90,80,100]
sum = 0
for i in list :
    sum += i
avg = sum/3
print("kor : 90\nmat : 80\neng : 100\nsum = {}\navg = {}".format(sum,round(avg)))