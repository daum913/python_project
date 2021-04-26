# 문제 6

# 두 정수를 변수 2개에 각각 담고 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램을 작성하시오
# 입력 예 : 35 10
# 출력 예 : 35/10 = 3...5

num1 = int(input("첫 번째 정수를 입력하세요 :"))
num2 = int(input("두 번째 정수를 입력하세요 :"))
result = num1//num2
result2 = num1%num2
print(num1,"/",num2,"=",result,"...",result2)