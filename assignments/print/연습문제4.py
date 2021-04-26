


# 두 변수에 논리값(true, false)을 각각 임의로 대입하고, 논리합 or 논리곱 and 의 결과를 출력하시오
# 입력 예 : FALSE true
# 출력 예 : FASLE OR TRUE --> TRUE
#         FALSE AND TRUE --> FALSE

a = False
b = True
plus = a or b
mul = a and b
print("논리합 {0} or {1} => {2}\n논리곱 {0} and {1} => {3}".format(a,b,plus,mul))