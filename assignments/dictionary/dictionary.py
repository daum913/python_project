

dic = {"melona" : [1000,10], "pollapo" : [1200,7],"ppanppare" : [1800,6], "tankboy" : [1200,9], "hothungint" : [1200,4], "worldcon" : [1500,3]}
dic2 = ["melona","pollapo","ppanppare","tankboy","hothunting","worldcon"]
for i in dic :
    for x in range(0,7) :
        print("아이스크림 이름 : {}, 희망 가격 : {}, 남은 수량 :{} ".format(dic2[x],(dic[i])[0],(dic[i])[1]))