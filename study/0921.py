# import matplotlib.pyplot as plt
# import csv
# month=['mar', 'apr','may', 'jun','jul']
# f = open("card.csv", encoding="UTF-8")
# data=csv.reader(f)
# next(data)
# data=list(data)
#
# spend=0
# for row in data:
#     if row[-1]=='전표매입':
#         payment=int(row[-3])
#         spend+=payment
# print(spend)
#
# plt.figure(dpi=100)
#
# plt.title('10~12월 택시/배달 음식 지출 현황')
#
# plt.plot(['10월', '11월', '12월'],deli,color='indigo',label='배달음식 지출액')
# plt.plot(['10월', '11월', '12월'],taxi,color='indigo',label='배달음식 지출액')

#
# import matplotlib.pyplot as plt
# import csv
#
# time = [0 for i in range(24)]
# population = [0 for i in range(24)]
# p_avg = [0 for i in range(24)]
# p = 0
# f = open("local.csv", encoding="UTF-8")
# data = csv.reader(f)
# next(data)
# data = list(data)
# for row in data:
#     if int(row[2]) == 11680545:
#         time = int(row[1])
#         p=float(row[3])
#         for i in range(24):
#             if time == i:
#                 population[i] += p
#
# s_time = [i for i in range(24)]
#
# for i in range(24):
#     p_avg[i] = population[i] / 31
#
# plt.plot(s_time, p_avg)
# plt.show()

import folium

# icon=folium.Icon(icon='모양')

lat, long=37.52860, 126.93431
map_y=folium.Map([lat,long],zoom_start=15)
folium.Marker([lat, long]).add_to(map_y)


for i in range(5):
    folium.Marker(
        [37.52860, 126.93431], tooltip='여의도 한강공원',
        icon=folium.Icon(color='pink', icon='home', prefix='fa')
    ).add_to(map_y)
map_y.save("D:\pyStudy\map.html")

lat1, log1=37.52860, 126.93431 #여의도 한강 공원
lat2, log2=37.52400, 126.91889 #여의도 공원
lat3, log3=37.51865, 126.92041 #샛강 생태 공원

lat=[lat1, lat2, lat3]
log=[log1, log2, log3]
title=['여의도 한강공원', '여의도 공원', '샛강 생태 공원']

























