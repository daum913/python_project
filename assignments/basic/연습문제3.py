# 문제 3
# 조건1 문자열을 입력받고 정수를 입력받아서 문자열의 맨 뒤부터 정수만큼 출력하는 프로그램을 작성하시오
# 조건 2 입력받은 정수가 문자열의 길이보다 크다면 맨 뒤부터 맨 처음까지 모두 출력한다

word = input("문자열을 입력하시오 : ")
num = int(input("정수를 입력하세요 : "))
word2 = word[::-1]
if num > len(word) :
    print(word2)
else :
    print(word2[0:num])




