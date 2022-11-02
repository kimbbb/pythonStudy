import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
df2=pd.read_csv('survey.csv')
df2.head()

male=df2.income[df2.sex=='m']
female=df2.income[df2.sex=='f']

ttest_result=stats.ttest_ind(male, female)
ttest_result
if ttest_result[1]>.05:
    print('p-value는 95% 수준에서 유의하지않음')
else:
    print('p-value는 95% 수준에서 유의함')