# 문제 8

# 민수와 가영이의 키와 몸무게를 각각 변수에 담고, 민수가 키도 크고 몸무게도 크면 TRUE를 그렇지 않으면 FALSE를 출력하는 프로그램을 만드시오.
# 입력 예>
# 민수 - 150 35
# 가영 - 140 35
# 출력 예> 
# FALSE

weight_m = int(input("민수의 몸무게를 입력하라 : "))
height_m = int(input("민수의 키를 입력하라: "))
weight_k = int(input("가영의 몸무게를 입력하라 : "))
height_k = int(input("가영의 키를 입력하라 : "))

if weight_m>weight_k and height_m>height_k :
    print("TRUE")
else :
    print("FALSE")