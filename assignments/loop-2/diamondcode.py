# diamond code
# ter a floor of diamond(odd)[quit: -1]: 3
#   *  
#  *** 
#   *  
# Enter a floor of diamond(odd)[quit: -1]: 1
# *
# Enter a floor of diamond(odd)[quit: -1]: 5
#     *    
#    ***   
#   *****  
#    ***   
#     *    
# Enter a floor of diamond(odd)[quit: -1]: 7
#       *      
#      ***     
#     *****    
#    *******   
#     *****    
#      ***     
#       *      
# Enter a floor of diamond(odd)[quit: -1]: -1
n = int(input("정수를 입력하세요 : "))
for i in range (1,n+1) :
     print(" "*(n-i),"*"*(2*i-n)," "*(n-i),sep="")
for i in range (n-1,0,-1) :
     print(" "*(n-i),"*"*(2*i-n)," "*(n-i),sep="")