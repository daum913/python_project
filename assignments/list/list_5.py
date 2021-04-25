# 문제 5.

# 10개의 정수를 입력받아 그 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
# 입력 예: 5 10 8 55 6 31 12 24 61 2
# 출력 예: 2

list_1 = []
for i in range(10) :
  num = (input("정수를 입력하세요 : "))
  list_1.append(num)
print(min(list_1))