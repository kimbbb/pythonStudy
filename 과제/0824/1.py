name=input('이름은 무엇입니까? : ')
kg=int(input('몸무게를 kg단위로 입력하세요. : '))
cm=int(input('키를 cm단위로 입력하세요. : '))
cm=cm/100
bmi=kg/(cm**2)
inbody=0

if bmi<18.50:
    inbody='저체중'
elif 18.50<bmi and bmi<24.99:
    inbody='정상'
elif 24.99<bmi and bmi<=29.99:
    inbody='과체중'
elif bmi>30:
    inbody='비만'


print(name+'의 BMI는 ',round(bmi,2),'이며, 현재 '+name+'의 상태는 ',inbody,'입니다.', sep='')
