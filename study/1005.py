#가짜 점쟁이
# date=input().split()
# sum=0
# for i in range(3):
#     sum+=int(date[i])
#
# a=[int(date) for date in str(sum)]
# if a[-3]%2==0:
#     print('대박')
# else:
#     print('중박')

# mon=[30,31,29,28]
# a=list(map(int, input().split()))
# y=0
# for i in range(len(a)):
#     if a[0]%400==0:
#         y=1
#     elif a[0]%4==0 and a[0]%100!=0:
#         y=1
#
#     if y==1:
#         if a[1]==2:
#             print(mon[2])
#         elif a[1] <= 7 and a[1] % 2 != 0:
#             print(mon[1])
#         elif a[1] > 7 and a[1] % 2 == 0:
#             print(mon[1])
#         else:
#             print(mon[0])
#     else:
#         if a[1]==2:
#             print(mon[3])
#         elif a[1] <= 7 and a[1] % 2 != 0:
#             print(mon[1])
#         elif a[1] > 7 and a[1] % 2 == 0:
#             print(mon[1])
#         else:
#             print(mon[0])



# a,b=map(int, input().split())
# sum=0
#
# if a>b or a<=0 or b>500 :
#     c=1
# else:
#     for i in range(a,b+1):
#         if i%2==0:
#             sum-=i
#         elif i%2!=0:
#             sum+=i
#
#
# if c==1:
#     print('다른 숫자를 입력해주세요')
# else:
#     print(sum)

#회문 출쳑
#앞으로 읽으나 뒤로 읽으나 똑같은 문장을 회문이라고 한다.
# 한 숫자를 입력받아 그 숫자와 그 숫자를 뒤집은 수를 더했을 때 회문이 되면 yes, 아니면 no 출력
# a=input()
# b=a[::-1]
# sum1=str(int(a)+int(b))
# if sum1 == sum1[::-1]:
#     print('yes')
# else:
#     print('no')

# import sys
# sys.setrecurionlimit(200)

# count=0
# k,n=map(int, input().split())
# while True:
#     count+=k//n
#     k=k%n+k//n
#
#     if k<n:
#         print('남은 도장 수 :',k)
#         break
# print('마실 수 있는 아메리카노 수 :',count)

# a=list(input().split())
# for i in range(len(a)):
#     b = [a[i] for a[i] in str(a[i])]
#     print(b[0].upper(), end='')

#Create the highest grandest vision possible for your life because you become what you believe
#
# a = {}
# for i in input().split():
#     if i in a:
#         a[i] += 1
#     else:
#         a[i] = 1
# print(a)


# def isalpha(a):
#     if ord(a) >= ord('A') and ord(a) < ord('Z') or ord(a) >= ord('a') and ord(a) <= ord('z'):
#         return True
#     else:
#         return False
# def isdigit(a):
#     if ord(a) >= ord('0') and ord(a) <= ord('9'):
#         return True
#     else:
#         return False
# def isspace(a):
#     if a == ' ':
#         return True
#     else:
#         return False
#
# a={
#     'digits':0,
#     'spaces':0,
#     'alphas':0
# }
#
# sum=0
# for i in input():
#     if isspace(i):
#         a['spaces'] += 1
#     if isdigit(i):
#         a['digits'] += 1
#     if isalpha(i):
#         a['alphas'] += 1
# print(a)

# a=()
# sum=0
# for i in range(1,100,2):
#     a=a+(i,)
#     sum+=i
#
# print(sum)

# a = input().split()
# count=0
# for i in range(15):
#     print(a[i])
#     # if a[i]==0:
#     #     a.pop()
#     # if a[i]//a[i]==1:
#     #     count+=1
# print(count)

count=0
A=int(input())
B=int(input())
C=int(input())
sum=A+B
while True:
    count+=sum//C
    sum=sum%C+sum//C

    if sum<C:
        break
print(count)

