# import numpy as np
# a = np.array([[2,3],[5,2]])
# d=np.array([[1,2,3,4,5],[2,3,4,5,6,7],[5,7,8,9,9]])
#
# print(a.dtype)
# print(d.dtype)
#
# d=d.astype('float64')
# print(d)
#
# print(d[0][0])
# print(d[1,2])
#
# print(d[1:,3:])
#
# np.zeros((2,10))
# print(d)

# d=np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
# d_list = [[1,2,3,4,5],
#           [2,4,5,6,7],
#           [5,7,8,9,9]]
#
# d_list[:2]=0
# d[:2]=0
#
# print()


# import pandas as pd
#
# data = {'name':['Mark', 'Do', 'Suho', 'Minji'],
#         'age':[26,30,32,18],
#         'score':[70, 90, 80, 100]}
#
# df=pd.DataFrame(data)
# print(df)
# print(df.sum())
# print(df.mean())


# import pandas as pd
#
# df = pd.read_csv('apt.csv', encoding='cp949')
#
# df.head()
# # print(df.tail())
# # print(df.시군구)
# # print(df.전용면적 > 80)
# # print(df[df.전용면적>80])
# # print(df.거래금액[(df.전용면적>80) & (df.거래금액<15000)])
# # print(df.거래금액[(df.전용면적>80) | (df.거래금액<15000)])
# # print(df.loc[:10, ['단지명','거래금액']])
# # print(df.head(11))
# # print(df.loc[:,['단지명','거래금액']])
# # df.head()
# # df.loc[:10,['단지명', '전용면적','거래금액','단가']]
# # df.sort_values(by='거래금액', ascending=False).loc[:,('전용면적','시군구')
# # >40000]
#
# df.시군구.str.find('강릉')
# df[df.시군구.str.find('강릉')>-1]

# import pandas as pd
# # df=pd.read_csv('titanic.csv')
# # df.describe()
# # df.dtypes
# # print(df)
#
# dfi=pd.read_csv('titanic.csv', index_col=0)
# dfi.to_excel('titanic_index.xlsx')
#
# print(dfi.Name)

import pandas as pd
df=pd.read_csv('countries.csv')
df1=pd.DataFrame({'code':["CA"], 'country':['Canada'], 'area':[9984670],})
df2=df.append(df1, ignore_index=True)
df2.drop(index=2,axis=0, inplace=True)
df2.drop(['capital'], axis=1, inplace=True)
print(df2)
