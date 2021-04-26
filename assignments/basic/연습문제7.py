# 문제 7 

 # 두 개의 문자열 a 와 b 한 개의 정수 n 을 입력받아서 a 에 b를 연결하고,
 #  변경된 문자열 a에서 n개의 문자를 b에 복사한 후  a 와 b 를 출력하는 프로그램을 작성하시오
 # banana, apple, 3 -> bananaaple -> banle
 
word_a = input("첫번째 단어를 입력하시오 : ")
word_b = input("두번째 단어를 입력하시오 : ")
num = int(input (("정수를 입력하시오 : ")))

a_b = str(word_a)+str(word_b) #bananaapple
print(a_b)

mix = a_b[0:num] # if num=3, a_b = ban

word_b2 = word_b[num:len(word_b)+1]

final = mix + word_b2
print(final)
# len(word_b) #5

# result = word_b[(len(word_b))-num : num]
# print(result)
