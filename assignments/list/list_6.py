# 문제 6.

# 10개의 정수를 입력받아 100 미만의 수 중 가장 큰 수와 100 이상의 수 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
# 입력 예: 88 123 659 15 443 1 99 313 105 48
# 출력 예: 99 105

list_1 = []
list_2 = []
som = 0
for i in range(10) :
  number =int(input("정수를 입력하세요 : "))
  som += number
  
  if number < 100 :
    list_1.append(number)
  elif number >= 100 :
    list_2.append(number)  
print(max(list_1), min(list_2))