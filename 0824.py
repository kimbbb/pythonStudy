# import turtle
#
# t=turtle.Turtle()
# t.shape("turtle")
#
# # t.forward(100)
# # t.left(90)
# # t.forward(50)
#
# # t.forward(100)
# # t.left(120)
# # t.forward(100)
# # t.left(120)
# # t.forward(100)
#
# colors=["red","purple","blue", "green", "yellow", "orange"]
# t=turtle.Turtle()
#
# turtle.bgcolor("black")
# t.speed(10)
# t.width(3)
# length=10
#
# while length<300:
#     t.forward(length)
#     t.pencolor(colors[length%6])
#     t.right(86)
#     length+=5
#
# turtle.mainloop()
# turtle.bye()
#

# #이름, 생년월일, 나이계산, 전화번호
# name=input('이름을 입력해주세요 : ')
# birth=input('생년월일 8자리를 입력해주세요 : ')
# call=input('전화번호를 입력해주세요 : ')
# a=birth[0:4]
# a=int(a)
# old=2023-a
# print()
# print(name,'님의 나이 (',old,')세에 맞는 추천 상품은 빵입니다~')

# price=int(input())
# if price<100:
#     a=price/10
#     print(price-a)
# else:
#     b=price/15
#     print(round(price-b,1))

# print('=========================')
# print('메뉴 1번: 치즈버거')
# print('메뉴 2번: 치킨버거')
# print('메뉴 3번: 불고기버거')
# print('=========================')
#
# a=int(input('메뉴를 선택하세요 : '))
# if a==1:
#     print('치즈버거')
# elif a==2:
#     print('치킨버거')
# elif a==3:
#     print('불고기버거')
# else:
#     print('잘못입력하셨습니다')
