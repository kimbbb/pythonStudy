#원의 면적
# a=int(input())
# area=a*a*3.14
# print(area)

#조건문

#배송비 계산 프로그램
# price=int(input())
#
# if price>20000:
#     shop=0
# else:
#     shop=3000
# print(price)
# print(shop)

# x=int(input())
# y=3
# max=(x if x>10 else y) #참이면 x반환 거짓이면 y
# print(max)

#홀짝구하기
# a=int(input())
# if a%2==0:
#     print('짝수입니다')
# else:
#     print('홀수입니다')


# a=[]
# b=int(input())
# for i in range(b):
#     c=input()
#     a.append(c)
#     print(a)


#리스트 항목 변경
# a=['gkdl', 'gpffh', 'zz']
# a.pop() #삭제
# a[-1]='하이' #항목 변경
# a.append() #항목 추가
# a.insert(2,'하이') #원하는 자리 항목 추가

#팩토리얼
# a=int(input())
# sum=1
# for i in range(1,a+1):
#     sum*=i
# print(sum)

#방정식 해 구하기
# count=int(input())
# start=1.0
# end=2.0
#
# for i in range(count):
#     a=start+i*((end-start)/count)
#     f=(a**2-a-1)
#     if abs(f-0.0)<0.01:
#         print(a)

#구구단
# for i in range(1,10):
#     print(9,'*',i,'=',9*i)


#숫자 맞추기 게임
# import random
# a=random.randint(1,101)
# count=0
# print(a)
# for i in range(a):
#     b=int(input())
#     count+=1
#     if a>b:
#         print('낮음')
#     elif a<b:
#         print('높음')
#     else:
#         print('축하합니다.','시도 횟수',count)

# import random
#
# while True:
#     a = random.randint(1, 101)
#     b = random.randint(1, 101)
#
#     print(a,'+',b,'=',end=' ')
#     c=int(input())
#     if c==a+b:
#         print('잘했어요')
#     else:
#         print('틀렸어요. 하지만 다음 번엔 잘할 수 있죠?')
#         break

#로그인
# while True:
#     pw=input()
#
#     if pw=='password':
#         print('로그인 성공')
#         break

#별찍기
# for i in range(1,6):
#     for j in range(i):
#         print('*',end='')
#     print()

#주사위 합이 6이 되는 경우
# for i in range(1,7):
#     for j in range(1,7):
#         if i+j==6:
#             print(i, j)

#모든 조합 출력
# a=['kim','park','lee','choi']
# b=['korean','french', 'american']
#
# for i in a:
#     for j in b:
#         print(i,'이',j,'식당을 방문')

#함수
# def a(b):
#     c=1*2+b
#     return c
#
# d=a(int(input()))
# print(d)

# def sum(b):
#     c = 0
#     for i in range(len(b)):
#         c+=b[i]
#     return c
#
# s=sum(list(map(int, input().split())))
# print(s)

# a=[]
# def long(b):
#     for i in range(T):
#         c=len(b)
#         a.append(c)
#         return a
#
# T=int(input())
# for j in range(T):
#     N=input()
#     long(N)
#
# print(a)

# N=int(input())
# for i in range(N):
#     A,B=map(int, input().split())
#     if A>B:
#         print(A)
#     elif A<B:
#         print(B)
#     else:
#         print(123456789)

#반지름 값 구하기
# def area(radius):
#     aarea=3.14*radius**2
#     return aarea
#
# result=area(3)
# result2=area(20)
#
# print(result, result2)

# def pizza1(radius):
#     pi=3.14*radius**2
#     return pi
#
# def pizza2(radius):
#     pizza=(3.14*radius**2)*2
#     return pizza
#
# a=pizza1(30)
# b=pizza2(20)
# print(a, b)

# def pizza(radius):
#     pi=3.14*radius**2
#     return pi
#
# print(20,'=',pizza(20)+pizza(20))
# print(30,'=',pizza(30))

# def sum(start, end):
#     sum=0
#     for i in range(start, end+start):
#         sum+=i
#     return sum
#
# print(sum(1,10))
# print(sum(1,20))


# def sum(*num):
#     sum=0
#     for i in num:
#         sum+=i
#     return sum
# print(sum(10,20))
# print(sum(10,20,30))

# a=[]
# sum=0
# max=0
# min=100
# count=0
# for i in range(5):
#     b=int(input())
#     a.append(b)
#
# for j in range(len(a)):
#     sum+=a[j]
#     p=sum/5
#
#     if a[j]>max:
#         max=a[j]
#
#     if a[j]<min:
#         min=a[j]
#
#     if a[j]>=80:
#         count+=1
# print(p,max,min,count)

# a=[1,2,3,4,5]
# for i in range(len(a)):
#     print(a[i], end=' ')
#
# for j in a:
#     print()
#     print(j, end=' ')

# a={'id':1,'name':'kim'}
# a[1]='kimmin' #추가
# a['id']=2 #수정
# del a[1] #삭제
# print(a)



