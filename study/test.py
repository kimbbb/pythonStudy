#1
# a=[]
# for i in range(2020,2100):
#     if i%400==0:
#         a.append(i)
#     if i%4==0 and i%100!=0:
#         a.append(i)
#     if len(a)==5:
#         break
# print(a)

#2
# a={}
# b=[]
# for i in range(1,101):
#     for j in range(1,101):
#         if i%j==0:
#           a[i]+=1
# for x in a:
#     if a.values()>2:
#         b.append(a.keys())
# print(b)


#3
# print('날짜를 입력하세요.(월과 일)')
# while True:
#     a=int(input('월을 입력하세요(1부터 12사이의 값) : '))
#     if a<1 or a>12:
#         continue
#
#     if a<8 and a%2!=0:
#         b=int(input('일을 입력하세요(1부터 31사이의 값) : '))
#         if b < 1 or b > 31:
#             continue
#         else:
#             break
#     elif a>7 and a%2==0:
#         b=int(input('일을 입력하세요(1부터 31사이의 값) : '))
#         if b < 1 or b > 31:
#             continue
#         else:
#             break
#     elif a<8 and a%2==0:
#         b=int(input('일을 입력하세요(1부터 30사이의 값) : '))
#         if b < 1 or b > 30:
#             continue
#         else:
#             break
#     elif a>7 and a%2!=0:
#         b=int(input('일을 입력하세요(1부터 30사이의 값) : '))
#         if b < 1 or b > 30:
#             continue
#         else:
#             break
#     elif a==2:
#         b=int(input('일을 입력하세요(1부터 28사이의 값) : '))
#         if b < 1 or b > 28:
#             continue
#         else:
#             break
#
# print('입력된 날짜는 ',a,'월 ',b,'일입니다', sep='')

#4
a={}
count=0
b='I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low Create the highhest grandest vision possible for yout life becaus you become what you believe'
b=b.lower()
c=list(b.split())
for i in c:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

    if a[i]>1:
        del a[i]
    else:
        count+=1

print(a)
print('사용된 단어의 개수 : ',count)

#5
# a=list(map(int, input('버섯 10개의 점수를 순서대로 입력하시오 : ').split()))


#6
# n=int(input('방문할 가게의 수를 입력하시오 : '))
# a=list(map(int, input('방문할 가게의 일직선 좌표',n,'개를 입력하시오 : ').split()))
#
# for i in range(n):
#


