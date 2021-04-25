# 문제 4.

# 아래와 같이 나라 이름을 출력하고 숫자를 입력받아 해당하는 나라의 수도를 출력하는 작업을 반복하다가 해당하는 번호 이외의 숫자가 입력되면 "none"라고 출력한 후 종료하는 프로그램을 작성하시오.
# 각 나라의 수도 :
# 대한민국 = 서울(Seoul)
# 미국 = 워싱턴(Washington)
# 일본 = 동경(Tokyo)
# 중국 = 북경(Beijing)
# 예시 입력 예:
# Korea
# USA
# Japan
# China number? 1
# 출력 예: Seoul
# Korea
# USA
# Japan
# China number? 5

country = ["1. Korea", "2. USA", "3. Japan", "4. China"]
capital = ["Seoul", "Washington", "Tokyo", "Beijing"]
print(country)
i = 1
while i < 5  :
    num = int(input("정수를 입력하세요 : "))
    if num<5 :
        print(capital[num-1])

    elif num >= 5 :
        print("None")
        break