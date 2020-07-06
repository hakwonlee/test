# def order():
#     print("음료를 주문하시겠습니까")
#     drink=input()
#     print(drink+"가 나왔습니다")
# order()



# def order(drink2,food):
#     print("음료를 주문하시겠습니까")
#     drink=input()
#     print(drink+"가 나왔습니다")
#     print('추가로',drink2,food,'가 나왔습니다.')
# order('콜라','빵')


def order():
    print("음료를 주문하시겠습니까")
    drink=input()
    
    if drink=="콜라" : 
        print("콜라가 나왔습니다.")
        return
    else :
        print(drink+"가 소신됬습니다.")

order()
