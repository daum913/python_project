# 문제 2.

# 자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력하는 프로그램을 작성하시오.
# 입력 예: 3

#     1
#   1 2
# 1 2 3

#     1
#   1 3
# 1 3 5

num = int(input("자연수를 입력하세요 : "))
for x in range(1,num+1) :
    a = 1
    for y in range(1,num-x+1) : #공백출력
        print(" ",end="")
    for y in range(1,x+1) :
        print(a,end="")
        a += 1
    print()
# ________________________________________    
num = int(input("자연수를 입력하세요 : "))
for x in range(1,num+1) :
    a = 1
    for y in range(1,num-x+1) : #공백출력
        print(" ",end="")
    for y in range(1,x+1) :
        print(a,end="")
        a += 2
    print()
  