# 문제 12.

# 복호화 키와 암호 문자를 입력으로 받아 원문을 구하는 프로그램을 구현하시오. 복호화 키는 26개의 소문자로 주어지며, a,b,c,d... 를 순서대로 복호화 키 문자로 대치한다는 것을 뜻한다.
# 예를 들어, 복호화 키가 "eydbkmiqugjxlvtzpnwohracsf" 와 같이 주어진다고 하자,
# 그러면 이는 다음과 같다 - a 문자는 e, b 문자는 y, ..., z 문자는 f로 바꿔줌.
# 암호화 된 문자는 대소문자 혹은 공백이 올수 있고 대소문자는 대문자로 소문자는 소문자로 치환 규칙에 맞게 출력하고 ,
# 공백문자는 그대로 출력한다.
# 입력 예:
# eydbkmiqugjxlvtzpnwohracsf
# Kifq oua zarxa suar bti yaagrj fa xtfgrj
# 출력 예:
# Jump the fence when you seeing me coming

string = input("문장을 입력하세요 : ")
key1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
key2 = input("복호화 문자를 입력하세요 :")

key2_2 = key2.upper() #대문자는 포함이 되어있지않기 때문에 대문자 변수를 만들어서(key2:복호화문자)와 더해주어야한다.
key3 = key2 + key2_2
transtab = string.maketrans(key1,key3)
print(string.translate(transtab))#translate 함수를 써 주어야 해석된 문장이 나온다.