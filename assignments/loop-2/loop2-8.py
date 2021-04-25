# 문제 8.

# 소수(prime number)란 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.
# 자연수 M과 N을 입력받아 M부터 N까지 소수의 개수를 구하여 출력하는 프로그램을 작성하시오.
# M이상 N이하의 자연수 중 소수가 몇 개인지 구하여 출력한다.
# 입력 예: 10 100
# 출력 예: 21
m = int(input("첫 번째 자연수를 압력하세요 : "))
n = int(input("두 번째 자연수를 압력하세요 : "))
num = 0
if n > m :
    for i in range(m,n+1) :
        a = 0
        for b in range(2,i) :
            if i % b == 0 :
                a = 1
        if a == 0 :
            num = num+1         
elif n < m :
    for i in range(n,m+1) :
        a = 0
        for b in range(2,i) :
            if i % b == 0 :
                a = 1
        if a == 0 :
            num = num+1
print(num)