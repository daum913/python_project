# 문제 5.

# 리스트을 선언한 후 정수를 차례로 입력 받다가 -1이 입력되면 입력을 중단하고, -1을 제외한 마지막 세 개의 정수를 출력하는 프로그램을 작성하시오.
# 입력받은 정수가 -1을 제외하고 3개 미만일 경우에는 -1을 제외하고 입력받은 정수를 모두 출력한다.
# 입력 예: 30 20 10 60 80 -1
# 출력 예: 10 60 80

list_1 = []
num = 1
while num != -1 :
  num= int(input("정수를 입력하세요 : "))
  list_1.append(num)
  if num == -1 :
    break

list_1.reverse()
list_1.remove(-1)
if len(list_1) <= 3 :
    list_1.reverse()
    print(list_1)
elif len(list_1) > 3 :
    list_2 = list_1[0:3]
    list_2.reverse()
    print(list_2) 