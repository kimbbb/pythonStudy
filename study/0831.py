# list = []
# list.append(1)
# list.append(2)
# list.append(6)
# list[-1]=2
# print(list)

# for i in 리스트(range()) :

# a=int(input())
# sum=1
# for i in range(1, a+1):
#     sum*=i
# print(sum)

# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i=i+1
# print(sum)

# a=int(input())
# for i in range(1, 10):
#     print(a,'*',i,'=',a*i)

# for i in range(1, 6):
#     for j in range(1, 6):
#         if j+i==6:
#             print(i,j)


# a=int(input())
# b=int(input())
# def pizza(a):
#     return a*a*3.14
# def pizza(b):
#     return b*b*3.14
#
# print(pizza(a)*2)
# print(pizza(b))

# rate=int(input())
# hour=int(input())
#
# def weeklyPay(rate, hour):
#     if hour<30:
#         cash = rate * hour
#         return cash
#     elif hour>30:
#         n = (rate * 30)+((rate*1.5) * (hour - 30))
#         return n
#
# print(weeklyPay(rate, hour))


# import turtle as t
#
# def tur(turt):
#     for i in range(4):
#         t.forward(90)
#         t.left(90)
#     return turt
#
# print(tur(tur))
#
# t.shape('turtle')

# temps=[28,31,33,35,27,26,25]
# for i in range(len(temps)):
#     print(temps[i], end=',')
#
# temps=[28,31,33,35,27,26,25]
# for element in temps:
#     print(element, end=',')

# import random
# n=random.randint(1,10)
# print(n)
#
# import random as r
# n=r.randint(1,10)
# print(n)

# import random as r
# d=list(range(1,46))
# r.shuffle(d)
# print(d[:7])


# import random as r
#
# g=list(range(1,46))
# r.shuffle(g)
# x=g[:6]
# print('당첨번호 :',g[:6],'+', '[',g[6],']')
#
# good=0
# count=0
# for i in range(6):
#     a = int(input('입력 : '))
#
#     if a==x[i]:
#         count+=1
#
#     elif a==g[6]:
#         good+=1
#
# print()
# print('-'*40)
#
# if count==6:
#     print('1등')
# elif count==5 and good==1:
#     print('2등')
# elif count==5:
#     print('3등')
# elif count==4:
#     print('4등')
# elif count == 3:
#     print('5등')
# else:
#     print('꽝~~ㅋ')


