import csv
import matplotlib.pyplot as plt

f = open("card.csv", encoding="UTF-8")
data=csv.reader(f)
next(data)
data=list(data)

dic = {}

for row in data:
    if row[-1]=='전표매입':
        if row[-4] not in dic:
            dic[row[-4]]=int(row[-3])
        else:
            dic[row[-4]] += int(row[-3])

a=sorted([i for i in dic], key = lambda x: -dic[x])
b=[]
for i in range(10):
    b.append(a[i])

print(b)
mon=['10월', '11월', '12월']
plt.barh(mon, b)
plt.show()



