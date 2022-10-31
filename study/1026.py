# import pandas as pd

# nba=pd.read_csv('nba.csv', parse_dates=['Birthday'])
#
# pd.Series([1,2,3]).dtype
#
# nba.dtype
# nba.dtype.value_counts()
# nba.index
# nba.columns
# nba.ndim
# nba.shape
# nba.sample(3)
# nba.numique()
# nba.max()
# nba.min()
# nba.nlargest(n=4, columns="Salary")

# nfl=pd.read_csv('nfl.csv', parse_dates=['Birthday'])
# nfl.loc['New York Jets'].head()

import pandas as pd

sales=pd.read_csv("sales_by_employee.csv",
                  parse_dates=['Date']).head()
sales.tail()
# sales.pivot_table(index='Date')
# sales.pivot_table(index='Date', aggfunc='mean')
# sales.pivot_table(index='Date', aggfunc='sum')
# sales.pivot_table(index='Date',values='Revenue', aggfunc='sum')

# sales.pivot_table(
#     index='Date',
#     columns='Name',
#     values='Revenue',
#     aggfunc='sum',
#     fill_value=0
# )

# sales.pivot_table(
#     index = "Date",
#     columns = "Name",
#     values = "Revenue",
#     aggfunc = "sum",
#     fill_value = 0,
#     margins = True
# )

# sales.pivot_table(
#     index = "Date",
#     columns = "Name",
#     values = "Revenue",
#     aggfunc = "sum",
#     fill_value = 0,
#     margins = True,
#     margins_name = "Total"
# )

# sales.pivot_table(
#     index='Date',
#     columns='Name',
#     values='Revenue',
#     aggfunc='count',
# )

# sales.pivot_table(
#     index='Date',
#     columns='Name',
#     values='Revenue',
#     aggfunc=['sum','count'],
#     fill_value=0
# )

# sales.pivot_table(
#     index = "Date",
#     columns = "Name",
#     values = ["Revenue", "Expenses"],
#     fill_value = 0,
#     aggfunc = { "Revenue": "min", "Expenses": "min" }
# )
#
# print(sales)

# sales.head(1)
#
# video_game_sales = pd.read_csv("video_game_sales.csv")
# video_game_sales.head(1)
# video_game_sales.melt(id_vars = 'Name', value_vars = "NA").head()
# regional_sales_columns = ["NA", "EU", "JP", "Other"]
#
# video_game_sales.melt(
#     id_vars = "Name", value_vars = regional_sales_columns
# )

groups1=pd.read_csv("groups1.csv")
groups1.head()

groups2=pd.read_csv("groups2.csv")
groups2.head()

categories=pd.read_csv("categories.csv")
categories.head()

cities=pd.read_csv('cities.csv', dtype={'zip':'string'})
cities.head()

pd.concat(objs=[groups1, groups2])

print(len(groups1))
print(len(groups2))
print(len(groups1)+len(groups2))

pd.concat(objs=[groups1,groups2],ignore_index=True)
pd.concat(objs=[groups1,groups2],keys=['G1','G2'])
groups=pd.concat(objs=[groups1,groups2], ignore_index=True)
groups.head(1)
groups.merge(categories, how='left', on='category_id').head()
groups.merge(
    cities,how='outer',left_on='city_id', right_on='id'
)


outer_join=groups.merge(
    cities,
    how='outer',
    left_on='city_id',
    right_on='id',
    indicator=True
)

in_right_only=outer_join['_merge']=='right_only'
print(outer_join[in_right_only].head())

