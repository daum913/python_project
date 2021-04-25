# 보너스2

# 삼각형의 높이 N을 입력받아서 아래와 같이 문자 'A'부터 차례대로 왼쪽 대각선으로 채워서 삼각형 모양을 출력하는 프로그램을 작성하시오.
# 입력 예 : 5
#         A
#       B F
#     C G J
#   D H K M
# E I L N O

ascii = 65 #아스키넘버 65-90까지가 영어 대문자
n = int(input("삼각형의 높이를 입력하세요 : "))
for x in range(n):
    ascii_num = ascii + x
    x += 1
    print("  "*(n-x), end="")
    for y in range(1, x+1):
        print(chr(ascii_num), end=" ")
        ascii_num += n-y
    if ascii_num > 90:
            ascii_num -= 26 #대문자가 속해있는 아스키코드값을 넘어가면 반복을 위해 26을 빼준다.
    print()