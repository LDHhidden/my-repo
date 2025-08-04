print("채무 계산기")


name = input("이름: ")
end = False
money_list = []

while end == False:
    money = int(input("돈을 입력하세요: "))
    money_list.append(money)
    
    request = True
    while request == True:
        result = input("추가로 입력하실 건가요? (yes/no)\n")
        if result == "yes":
            request = False
            end = False
        elif result == "no":
            request = False
            end = True
        else:
            print("다시 입력해 주시기 바랍니다.")
    
print(money_list)
print(name+"에게 빌린 돈은 총"+str(sum(money_list))+"원")
"""TODO: 1.함수 및 모듈 사용해보기, 2. 데이터베이스에 연결하여 저장 3. 프로그램으로 제작"""