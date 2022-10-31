an=[]

def ans(a):
    an.append(a)
    return an

find=0
h=list(input().split(', '))
o=[list(input().split())]
k=input()

for j in range(len(o)):
    a=o[j]

for i in range(len(h)):
    b=h[i].split()
    
    for x in range(len(b)):
        if a[0]=='W' and a[1]=='T':
            if k==b[x]:
                t=ans(h[i])
            else:
                find+=1
                if find == len(b):
                    t=ans('empty')

    if a[1]=='F':
        t=ans(h[i])



print(t)


