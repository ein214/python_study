from random import choice

def rsp_num(name):
    if name == "가위":
        return 1
    elif name == "바위":
        return 2
    else:
        return 3

def rsp_winner(you, com):
    result = you - com
    if result == 0:
        txt = "비겼습니다."
    elif result in [-2, 1]:
        txt = "축하합니다. 당신이 이겼습니다"
    else : 
        txt = "컴퓨터가 이겼습니다."
    
    return txt
    


rsp_list = ['가위', '바위', '보']
rsp = input("가위바위보 게임입니다. 무엇을 낼지 입력해 주세요. :")

YOU = rsp
COM = choice(rsp_list)

print("사용자 : ",YOU)
print("컴퓨터 : ",COM)
print(rsp_winner(rsp_num(YOU), rsp_num(COM)))