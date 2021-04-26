# 문제 5

# 3개의 정수를 변수 3개에 담아 첫 번째 수가 가장 크면 TRUE 아니면 FASLE를 출력하고,
# 세 개의 수가 모두 같으면 TRUE 아니면 FALSE를 출력하는 프로그램을 작성하시오.
list = []
for i in range(3) :
    num = int(input("정수를 입력하세요 :"))
    list.append(num)
if list[0] == max(list) :
    print("TRUE")
else :
    print("FALSE")
if list[0] == list[1] == list[2] :
    print("TRUE")
else :
    print("FALSE")

