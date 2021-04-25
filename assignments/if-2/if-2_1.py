# 문제 1.

# "FizzBuzz"문제
# 1에서 100까지의 숫자를 출력하되,
# 만약 해당 숫자가 '3'으로 나누어지면 숫자 대신에 "Fizz"를 출력하고,
# 만약 해당 숫자가 '5'로 나누어지면 숫자 대신에 "Buzz"를 출력하며,
# 만약 해당 숫자가 '3'과 '5'로 모두 나누어지면 숫자 대신에 "FizzBuzz"를 출력
# 입력 예1: 5
# 출력 예1: "Buzz"
# 입력 예2: 3
# 출력 예2: "Fizz"
# 입력 예3: 15
# 출력 예3: "FizzBuzz"

num= int(input("1에서 100사이의 숫자를 입력하시오 : "))
if num%3 == 0 and num%5==0 :
  print('"FizzBuzz"')
elif num%5 == 0 :
  print('"Buzz"')
elif num%3 == 0 :
  print('"Fizz"')
else :
  print(num)