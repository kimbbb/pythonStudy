a=input()
sum=0
bc=0
cc=0
for i in range(len(a)):
    b=a[i].isupper()
    c=a[i].islower()
    d=ord(a[i])

    if b==True:
        bc+=1
    if c==True:
        cc+=1

    if len(a)>=8:
        if d>47 and d<58:
            if bc>=1 and cc>=1:
                sum+=1


if sum>=1:
    print('사용 가능한 패스워드입니다.')
else:
    print('사용할 수 없는 패스워드입니다. 다시 입력하세요!')



