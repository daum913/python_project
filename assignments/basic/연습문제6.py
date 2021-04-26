# 문제 6

# 20개 이하의 문자로 이루어진 10개의 단어와 한 개의 문자를 입력받아서
# 마지막으로 입력받은 문자로 끝나는 단어를 모두 출력하는 프로그램을 작성하시오.

list = []
list_2 = []
for i in range (10) :
    word = input("단어를 입력하세요 : ")
    list.append(word)
n = input("한 개의 문자를 입력하세요 : ")
for a in range (0,10) :
    if list[a][-1] == n :
        list_2.append(list[a])
print(list_2)