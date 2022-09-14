# heroes=["아이언맨", "토르", "헐크", "스칼렛 위치", "헐크"]
# print(heroes.index("헐크",3))

# heroes=["아이언맨", "토르", "헐크", "스칼렛 위치", "헐크"]
#
# if "헐크" in heroes:
#     print(heroes.index("헐크"))

# numbers=[10,3,7,1,9,4,2,8,5,6]
# ascending_numbers=sorted(numbers)
# print(ascending_numbers)

# numbers=[-7, 2, 3, 8, 6, 6, 75, 38, 3,2]
# ascending_numbers=sorted(numbers)
# print(ascending_numbers[-2])

# temps=[28,31,33,35,27,26,25]
# values=temps

# arr=[]
# for i in range(100):
#     if i%2==0 and i%3==0:
#         arr.append(i)
# print(arr)

# s=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# print(s)

# rows=3
# cols=5
#
# s=[]
# for row in range(rows):
#     s+=[0]*cols
#
# print("s =",s)

#

# #튜플
# #튜플_이름=(항목1, 항목 2...)
# fruits=()
# fruits=("apple", "banana","grape") #괄호 생략 가능


# n1=10
# n2=90
# n1,n2=(n2,n1)

# a=input()
# b=input()
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             print(a[i], end=' ')


# score_dic={
#     "Kim":[99,83,95],
#     "Lee":[68,45,78],
#     "Choi":[25,56,69]
# }
#
# print(score_dic)

import random

list_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
samplelist = random.sample(list_b, 4)

print(samplelist)