icecream = {"tankboy" : 1200, "ppangpare" : 1800, "worldcorn" : 1500, "melona" : 1000}
dic = list(min(zip(icecream.values(),icecream.keys())))
#zip함수: zip()의 첫번째 값에 의해 정렬이 이루어진다. 그래서 가격을 나타내는 values를 먼저 써준다. 
print(dic[1])
#이름만 출력해주기 위해 리스트로 만든후 이름에 해당하는 리스트 인덱스를 출력했다