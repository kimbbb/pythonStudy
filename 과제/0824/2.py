food, tip, plus, people=map(int, input('음식비용, 팁비율, 부가세비율, 식사비용을 나눌 사람의 수를 순서대로 입력해주세요. : ').split())
tip=food//tip
plus=food//plus
all=food+tip+plus
sum=all//people
print()
print('음식비용 :',food)
print('팁 :',tip)
print('부가세 :',plus)
print('식사 비용 나눌 사람 수 :',people)
print('각자 낼 돈 :',sum)
print('총액 :',all)