import random

win=0 # 승리횟수
lose=0 # 패배횟수

award = ['자동차','염소','염소'] #보상저장
random.shuffle(award) # 보상 리스트 섞어줌


for j in range(1000):
    first_check = random.randint(0,2) # 리스트 중 몇번을 선택하는지 정하기
    goat_location = [i for i, value in enumerate(award) if value == '염소'] #염소 위치 리스트에 저장


    if(goat_location[0]!=first_check): #내가 선택한 위치에 염소가 있는지 확인하는 구문, 선택한 위치 = 염소위치면 다른 염소위치를 알려줌
        presentation = goat_location[0] #사회자가 알려줄 염소위치를 변수에 저장한다
    else:
        presentation = goat_location[1]


    total_list = [presentation,first_check] #내가 처음에 선택한 위치와 알려준 염소위치의 리스트

    for i in range(3):# total_list에 없는걸 선택하는게 결국 선택위치를 바꾸는게 됨
        if i not in total_list:
            if award[i] == '자동차':
                win+=1
                break
            else:
                lose+=1
                break
                
print(win) # 승리 / 1000-win : 패배
