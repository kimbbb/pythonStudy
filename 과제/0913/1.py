#1
# a = [1, 2, 3, 4, 5]
# b = [1,3,3,4,5,6,7]
#
# c = set(a) & set(b)
# print(c)

#2

#3
# co=['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'T', 'T']
# m1=0
# m2=0
# max=0
#
# for i in range(len(co)):
#
#     if co[i]==co[i+1]:
#         print(0, end=' ')
#         m1+=1
#         m2=0
#         if max<m1:
#             max=m1
#     else:
#         print(1, end=' ')
#         m1=0
#         m2+=2
#         if max<m2:
#             max=m2
# print('최대 :',max)

#4
# colors = ["red", "green", "blue"]
# values = ["#FF0000", "#0080000", "#0000FF"]
# dictionary = dict(zip(colors, values))
# print(dictionary)

#5
# set1 = {10, 20, 30, 40, 50, 60}
# set2 = {30, 40, 50, 60, 70, 80}
#
# a=set1-(set1&set2)
# b=set2-(set1&set2)
# a.update(b)
# print(a)



#6
# m,w,d=map(int, input().split('/'))
# print(m,w,d,sep='')











