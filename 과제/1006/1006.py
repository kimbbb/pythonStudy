# a,b=map(int, input().split())
#
# def fun():
#     if a>b:
#         if a%2==0:
#             print('a는 짝수')
#         else:
#             print('a는 홀수')
#     else:
#         if b%2==0:
#             print('b는 짝수')
#         else:
#             print('b는 홀수')
#
# fun()

# h,w=map(int, input('키와 몸무게를 차례대로 입력 : ').split())
# bmi= w/(h**2/100)*100
# print('당신의 비만도는 ', round(bmi, 2),'입니다', sep='')
#
# if bmi<20:
#     print('저체중')
# elif bmi<25 and bmi>=20:
#     print('정상')
# else:
#     print('과체중')

# a=int(input('정수를 입력하시오 : '))
# for i in range(a):
#     for j in range(i+1):
#         print(j+1, end=' ')
#     print()

a=int(input()) #시작값
m=int(input()) #곱할값
d=int(input()) #더할 값
n=int(input()) #몇번쨰인지

for i in range(n-1):
    a=a*m+d
print(a)


