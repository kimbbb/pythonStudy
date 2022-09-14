import matplotlib.pyplot as plt
#
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
