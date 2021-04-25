# 문제 7.

# 학생들의 점수를 입력을 받다가 0이 입력되면 그 때까지 입력받은 점수를 10점 단위로 구분하여 점수대별 학생 수를 출력하는 프로그램을 작성하시오.
# 1명도 없는 점수는 출력하지 않는다.
# 입력 예: 63 80 95 100 46 64 88 0
# 출력 예: 
# 100 : 1 person
# 90 : 1 person
# 80 : 2 person
# 60 : 2 person
# 40 : 1 person
list = []
while True:
    score = int(input("점수를 입력하세요 : "))
    score2 = int(score/10)*10 #1의 자리 숫자 없애기
    list.append(score2)
    if score == 0 :
        break
list.remove(0) #입력된 0을 제거한다
set_list = sorted(set(list),reverse=True)
#내림차순으로 정리해주었다, set으로 변환해 중복을 제거해준다. 아래에서 딕셔너리의 키값으로 쓸 것이다.
ppl = []
for i in set_list :
    list.count(i)
    ppl.append(list.count(i))

result = dict(zip(set_list,ppl))
for a,b in result.items():
    print("{}:{}person".format(a,b))
    







    