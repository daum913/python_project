# 문제 2.

# “몸무게+100-키”를 비만수치 공식이라고 하자.
# 키와 몸무게를 자연수로 입력받아 첫 번째 줄에 비만수치를 출력하고, 비만수치가 0보다 크면 다음줄에 비만("Obesity")이라는 메시지를 출력하는 프로그램을 작성하시오.
# 입력 예: 155 60
# 출력 예:
# 5
# Obesity

height = int(input("키를 입력하세요 : "))
weight = int(input("몸무게를 입력하세요 : "))
bmi = weight+100 - height
if bmi > 0 :
  print(bmi)
  print("obesity")
else : 
  print(bmi)