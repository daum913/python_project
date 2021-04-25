# 문제 7.

# 가상의 두 사람(A, B)이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
# 입력 예: "가위" "바위"
# 출력 예: "B가 이겼습니다."

a = input("A님! 가위, 바위, 보 중 하나를 내세요 : ")
b = input("B님! 가위, 바위, 보 중 하나를 내세요 : ")
list = ["가위","바위","보"]
if a == list[0] and b == list[1] :
  print("B가 이겼습니다.")
elif a == list[0] and b == list[2] :
  print("A가 이겼습니다.")
elif a == list[1] and b == list[0] :
  print("A가 이겼습니다.")
elif a == list[1] and b == list[2] :
  print("B가 이겼습니다.")
elif a == list[2] and b == list[1] :
  print("A가 이겼습니다.")
elif a == list[2] and b == list[0] :
  print("B가 이겼습니다.")
else :
  print("무승부 입니다")
