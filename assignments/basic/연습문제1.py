# 문제 1

# 1야드는 91.44cm이고 1인치는 2.54cm 이다.
# 2.1야드와 10.5인치를 각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.
# 출력 예 : 
# - 1yd = 192.0cm
# - 10.5in = 26.7cm


yd = round(91.44*2.1,1)
inch = round(10.5*2.54,1)
print("2.1yd = {}cm\n10.5 in = {}cm".format(yd,inch))