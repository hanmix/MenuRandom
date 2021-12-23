import random, time

menu = []
cn = 'y'
# cnt = 0

# 반복해서 동작하기위한 while문
while (cn == 'y' or cn == 'Y'): 
    # 메뉴 추가
    while True: # 수정해주신 내용 : while cnt == 0: 을 기존의 True 값으로 받음(메뉴추가 부분부터 무한반복을 하기 위함)
        print(menu)
        item = input('메뉴를 추가해주세요. : ')
        if item == 'q':
            break
        else:
            menu.append(item)
    # 메뉴리스트를 집합으로 변경
    set_menu = set(menu)

    # 메뉴 삭제 
    while True: 
        print(set_menu)
        item = input('메뉴를 삭제해주세요. :')
        if item == 'q':
            break
        else:
            set_menu = set_menu - set([item])
            menu = list(set_menu) # 빈 리스트인 menu를 list(set(menu))와 같은 값으로 놓음으로써 무한반복 실행 시 빈 리스트에 최종 list 값이 출력되게 함
    print(set_menu)

    # 5초 카운트 후 랜덤 메뉴 출력  
    print('5초 후에 ', set_menu, ' 중에 하나를 선택합니다.') 
    for i in range(5, 0 , -1):
        print(i)
        if i == 5:
            time.sleep(1)
        elif i == 4:
            time.sleep(1)
        elif i == 3:
            time.sleep(1)
        elif i == 2:
            time.sleep(1)
        elif i == 1:
            time.sleep(1)
    print('오늘의 랜덤 메뉴는 ', random.choice(list(set_menu)), '입니다.')

    # 랜덤 결과를 처음부터 다시 출력(메뉴 추가로 이동) 또는 메뉴 정하기 종료
    cn = input('다시 하시겠습니까? (Y/N) : ')
    # cnt = 1 코드 입력 시 메뉴삭제부터 시작, cnt = 0 또는 코드를 작성하지않을 경우 메뉴추가부터 시작.
    while(cn != 'y' and cn != 'n' and cn != 'Y' and cn != 'N'):
        print('Y나 N만 입력하세요.')
        print('----------------------------------------------')
        cn = input('다시 하시겠습니까? (Y/N) : ')
    print('--------------------종 료--------------------')
