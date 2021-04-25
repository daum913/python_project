# 문제 3.

# 자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력되는 프로그램을 작성하시오.
# 입력 예 : 3
# 1 2 3
#   4 5
#     6
    
# 1 3 5
#   7 9
#     11    
n = int(input("자연수를 입력하세요 : "))
a = 1
for x in range(n,0,-1) :
    for y in range(1,n-x+1) :
        print(" ",end="")
    for y in range(1,x+1) :
        print(a, end="")
        a += 1
    print()
    # ______________________________
n = int(input("자연수를 입력하세요 : "))
a = 1
for x in range(n,0,-1) :
    for y in range(1,n-x+1) :
        print(" ",end="")
    for y in range(1,x+1) :
        print(a, end="")
        a += 2
    print()