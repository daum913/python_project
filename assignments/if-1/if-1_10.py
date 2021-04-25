# 문제 10.

# 공백을 포함한 문자열을 입력받아 각 단어로 분리하여 문자열 배열에 저장한 후 입력순서의 반대 순서로 출력하는 프로그램을 작성하시오. 문자열의 길이는 100자 이하이다.
# 입력 예: C++ Programing jjang!!
# 출력 예:
# jjang!!
# Programing
# C++

sentence = input("공백을 포함한 문자열을 입력하세요 : ")
sentence2 = (sentence).split(" ")
print(sentence2[::-1])