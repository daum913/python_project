# 문제 8.

# 10개의 정수를 입력받아 리스트에 저장한 후 내림차순으로 정렬하여 출력하시오.
# 입력 예: 95 100 88 65 76 89 58 93 77 99
# 출력 예: 100 99 95 93 89 88 77 76 65 58

list_1 = []
for i in range (10) :
  num = int(input("정수를 입력하세요 : "))
  list_1.append(num)
list_1.sort()
list_1.reverse()
print(list_1)