# 문제 1.

# 문자 10개를 저장할 수 있는 리스트를 만들고 10개의 문자를 입력받아 입력받은 문자를 이어서 출력하는 프로그램을 작성하시오.
# 입력 예: A B C D E F G H I J
# 출력 예: ABCDEFGHIJ

list1 = []
for i in range(10) :
    word =(input("문자를 입력하세요 : "))
    list1 += word

print(list1)
