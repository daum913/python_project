# 문제3.

# 초를 입력 받아서 시간과 분으로 변환하는 프로그램을 작성하시오.
# 입력 예: 3598
# 출력 예: 59분 58초

second = int(input("초를 입력하세요 : "))
min1 = second%60
min2 = second//60
print("{0}분 {1}초".format(min2,min1))