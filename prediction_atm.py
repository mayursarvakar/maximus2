import datetime as dt

import pandas as pd

df=pd.read_csv('S1BB005080002.csv')
# print(df.columns)
df2=df[['Terminal_ID','Tic_Rais_date_time','Sub_Category']]
df3=pd.DataFrame(df2.loc[df2['Sub_Category']=='Actionable query'])

# df3['occured']=1
df3['Tic_Rais_date_time']=pd.to_datetime(df3['Tic_Rais_date_time']).dt.date
# df3['new_date']=(df3.Tic_Rais_date_time).dt.month
# print(df3.columns)
print(type(df3))
# print(df3)
df4=df3['Tic_Rais_date_time'].value_counts().rename_axis('Date').reset_index(name='Actionable query')

df4['Date'] = pd.to_datetime(df4['Date'])
df4 = df4.set_index('Date')
df4.sort_index(inplace=True)
print(df4)
df4.to_csv('Actionable query_demo.csv')


# atm_name=df['Terminal_ID'][0]
# df['Tic_Rais_date_time'] = pd.to_datetime(df['Tic_Rais_date_time'])
# df['months'] = df.Tic_Rais_date_time.apply(lambda x: dt.datetime.strftime(x, '%b %Y')).tolist()
# #
# df = df.set_index('Tic_Rais_date_time')
# df.sort_index(inplace=True)
# subcat_unique = df['Sub_Category'].unique()
# sub_months_unique = df['months'].unique()
# sub_cat_list = []
# sub_month_list = []
# sub_count_list = []
#
# #   print(f"ID, Sub_cat   , Month    , Count ")
# #           index_var=0
# for j in subcat_unique:
#     index_var = 0
#
#     #     print(j)
#     for i in sub_months_unique:
#         index_var = index_var + 1
#         sub_cat = j
#         result = len(df[(df.Sub_Category == j) & (df.months == i)])
#         #         print(f"{index_var}, {sub_cat} , {i} , {result}")
#         sub_cat_list.append(sub_cat)
#         sub_month_list.append(i)
#         sub_count_list.append(result)
#
# month_wise_sub_cat_data = pd.DataFrame({
#     'Sub_category': sub_cat_list,
#     'Months': sub_month_list,
#     'Counts': sub_count_list})
#
#
#
# df2=month_wise_sub_cat_data
#
# df3=pd.DataFrame(data=None,index=df2['Months'].unique(),columns=df2['Sub_category'].unique())
# for i in df3.columns:
#     df3[i]=list(df2['Counts'].loc[df2['Sub_category']==i])
#
# print(df3)