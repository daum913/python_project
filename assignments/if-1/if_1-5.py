# 문제 5.

# 두 개의 실수를 입력받아 모두 4.0 이상이면 "A", 모두 3.0 이상이면 "B", 아니면 "C" 라고 출력하는 프로그램을 작성하시오.
# 입력 예1: 4.3 3.5
# 출력 예1: B
# 입력 예2: 4.0 2.9
# 출력 예2: C

num1 = float(input("첫 번째 실수를 입력하세요 : "))
num2 = float(input("두 번째 실수를 입력하세요 : "))
if num1 and num2 >=4.0 :
  print("A")
elif num1 and num2 >=3.0 :
  print("B")
else :
  print("C")