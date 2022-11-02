import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

excel=pd.read_excel("조사정보1.xlsx")
df=pd.DataFrame(excel)
df.head()
a=df.loc[[0]]
# print(df.loc[[0]])
gender=excel.loc[0]
print(gender.dtype)

a.isnull()
a.isnull().sum()
a.dropna()
# 결측치 찾아서 삭제


df1=pd.DataFrame(a)
df1.rename(columns={'설명':'male', '내용':'female'}, inplace=True)
print(df1)




