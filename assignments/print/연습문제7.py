# 문제 7

# 직사각형의 가로와 세로의 길이를 정수형 값 변수에 담고,
# 가로이 길이는 5 증가시키고, 세로이 길이는 2배하여 저장한 후
# 가로의 길이 세로의 길이 넓이를 차례로 입력하는 프로그램을 작성하시오.

# 입력 예 : 20 15
# 출력 예 
# width = 25
# lenght = 30
# area = 750

width = int(input("가로의 길이를 입력하세요 : "))
length = int(input("세로의 길이를 입력하세요 : "))
wid_2 = width+5
len_2 = length*2
area = wid_2 * len_2

print("width = {}\nlength = {}\narea = {}".format(wid_2,len_2,area))

