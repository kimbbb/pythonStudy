import matplotlib.pyplot as plt

#plt.plot([1,5,7,3,7])
# plt.title('월별판매실적')
# plt.rc('font', family='Malgun Gothic')
# month=['mar', 'apr','may', 'jun','jul']
# sales=[1,3,5,3,7]
# plt.plot(month,sales,color='red', )
# plt.show()

sales=[1,5,7,3,7]
month=['mar', 'apr','may', 'jun','jul']
plt.rc('font', family='Malgun Gothic')
plt.title('월별 판매 실적')
plt.bar(month,sales,color='b')
plt.show()

# sales=[1,2,3,3,3,5,7,7,8,10]
# plt.hist(sales,bins=30)
# plt.show()

# import random
# list=[]
# for i in range(10):
#     n=random.randint(0,10)
#     list.append(n)
# plt.hist(list, bins=10)
# plt.show()


# ladels=['A','B','AB','O']
# pie=(a.labels,autopct='%l.lf%%')
# plt.show()


# kor=[80,20,50,20,10,50,60,30,60]
# eng=[90,40,60,40,10,30,50,70,90]
# plt.scatter(kor,eng)
# plt.show()

# import random
# height=[]
# weight=[]
# score=[]
#
# for i in range(100):
#     a=random.randint(100,200)
#     b=random.randint(100,200)
#     c=random.randint(1,1000)
#     height.append(a)
#     weight.append(b)
#     score.append(c)
#
# plt.scatter(height,weight,c=score,s=score, cmap='rainbow',alpha=0.7)
# ladels=['A','B','AB','O']
# plt.colorbar(label='체육 점수')
# plt.show()


# import random
# kor=[]
# for i in range(10):
#  a=random.randint(0,101)
#  kor.append(a)
#
# plt.boxplot(kor)
# plt.show()

# singer=['A','B','C','D','E']
# week1=[42,58,19,92,84]
# week2=[53,52,48,98,73]
#
# plt.rc('font', family='Malgun Gothic')
# plt.title('오디션 프로그램 득표 현황')
# plt.plot(singer,week1,week2)
# plt.show()


# singer=['A','B','C','D','E']
# week1=[42,58,19,92,84]
# week2=[53,52,48,98,73]
#
# for i in range(5):
#     week1[i]=-week1[i]
# plt.rcParams['axes.unicode_minus']=False
# plt.rc('font', family='Malgun Gothic')
# plt.title('오디션 프로그램 득표 현황')
# plt.barh(singer, week1 )
# plt.barh(singer, week2)
# plt.show()

# import random
#
# height1=[]
# height2=[]
# weight1=[]
# weight2=[]
# score1=[]
# score2=[]
# for i in range(100):
#     a=random.randint(140,180)
#     b=random.randint(40,80)
#     c=random.randint(160,200)
#     d=random.randint(60,100)
#     e=random.randint(1,200)
#     f=random.randint(1,200)
#     height1.append(a)
#     weight1.append(b)
#     height2.append(c)
#     weight2.append(d)
#     score1.append(e)
#     score2.append(f)
#
# plt.rc('font', family='Malgun Gothic')
# plt.title('키와 몸무게의 상관관계')
# plt.scatter(height1, weight1,s=score1, color='crimson' ,alpha=0.7, label='group1')
# plt.scatter(height2, weight2, s=score2,color='indigo', alpha=0.7, label='group2')
# plt.legend()
# plt.show()

# import random
#
# kor=[]
# eng=[]
# for i in range(100):
#     a=random.randint(10,90)
#     b=random.randint(10,90)
#     kor.append(a)
#     eng.append(b)
# plt.rc('font', family='Malgun Gothic')
# plt.boxplot([kor,eng], labels=['국어', '영어'])
# plt.show()

# import csv
# f=open('card.csv')
# data=csv.reader(f)
# next(data)
# data=list(data)
#
# print(data[0])
# print(len(data))

data=[]
for row in data :
    print(row[0])

for row in data:
    print(row[-3])

for row in data:
    print(row[5],'에서',row[6],'원 사용')

for row in data:
    store = row[5]
    payment=row[6]
    print(store,'에서',payment,'원 사용')