# 보너스

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100이 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
# 이들 소수의 합은 620이고, 최소값은 61이 된다.

m = int(input("첫 번째 자연수를 입력하세요 : "))
n = int(input("두 번째 자연수를 입력하세요 : "))
prime = []
num = 0
if n > m :
    for i in range(m,n+1) :
        a = 0
        for b in range(2,i) :
            if i % b == 0 :
                a = 1
        if a == 0 :
            num = num+1
            prime.append(i)      
elif n < m :
    for i in range(n,m+1) :
        a = 0
        for b in range(2,i) :
            if i % b == 0 :
                a = 1
        if a == 0 :
            num = num+1
            prime.append(i)
result = sum(prime)
print("소수의 최소값은 {} 이고 소수의 합은 {} 이다.".format(min(prime),result))