# diamond code2
# mid: 0
# *
# ==================
# mid: 1
#  * 
# ***
#  * 
# ==================
# mid: 2
#   *  
#  *** 
# *****
#  *** 
#   *  
# ==================
# mid: 3
#    *   
#   ***  
#  ***** 
# *******
#  ***** 
#   ***  
#    *   
# ==================
# mid: 4
#     *    
#    ***   
#   *****  
#  ******* 
# *********
#  ******* 
#   *****  
#    ***   
#     *    
# ==================

n = int(input("정수를 입력하세요 : "))
for i in range (1,2*n) :
     print(" "*(2*n+1-i),"*"*(2*i-2*n+1)," "*(2*n+1-i),sep="")
for i in range (2*n,0,-1) :
     print(" "*(2*n+1-i),"*"*(2*i-2*n+1)," "*(2*n+1-i),sep="")
if n == 0 :
    print("*")

#diamond code-1 문제에서 n을 2*n+1로 바꿔주었다. 입력받은숫자 *2 +1 만큼 행이 생기기 때문.