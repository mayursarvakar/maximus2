from tkinter import *
import glob
from dash import html
import dash_table

import dash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import timedelta
import warnings
warnings.filterwarnings

atm_tamp = []
sub_cat_tamp = []
time_ser_tamp = []
class aveg_time():
    def avg_time_func(self,f):
        df = pd.read_csv(f'Atm_saprated_data//{f}.csv')
        df = df[['Tic_Rais_date_time', 'Numerical_Tic_Rais_date_time', 'Sub_Category', 'Terminal_ID']]
        atm_name1 = f.split("_")
        atm_name = atm_name1[-1].replace(".csv", "")
        print(f'\n=========================================={atm_name}==============================================')

        print(df[['Tic_Rais_date_time', 'Sub_Category', 'Terminal_ID']].head())
        #     print(df.columns)

        sub_unique = df['Sub_Category'].unique()
        for sub_unique_id in sub_unique:
            sub_cat_df = df.loc[df['Sub_Category'] == sub_unique_id]
            sub_cat_df['Tic_Rais_date_time'] = pd.to_datetime(sub_cat_df['Tic_Rais_date_time'])

            sub_cat_df = sub_cat_df.set_index('Tic_Rais_date_time')
            sub_cat_df.sort_index(inplace=True)




            sub_cat_df['Numerical_Tic_Rais_date_time'] = sub_cat_df.index

            sub_cat_df['Numerical_Tic_Rais_date_time_shit_1'] = sub_cat_df['Numerical_Tic_Rais_date_time'].shift(-1)

            sub_cat_df = sub_cat_df[:-1]

            sub_cat_df["Culculated_hours"] = sub_cat_df['Numerical_Tic_Rais_date_time_shit_1'] - sub_cat_df[
                'Numerical_Tic_Rais_date_time']

            sub_cat_df["Culculated_seconds"] = sub_cat_df['Culculated_hours'].dt.total_seconds()

            n = sub_cat_df['Culculated_seconds'].mean()

            if len(sub_cat_df) > 0:
                print(f'\n--------------------------{atm_name}_{sub_unique_id}--------------------------------------')

                n = str(timedelta(seconds=n))

                print(f'Average time when can {sub_unique_id} happen  afrer servicing on {atm_name}: {n}')

                atm_tamp.append(atm_name)
                sub_cat_tamp.append(sub_unique_id)
                time_ser_tamp.append(n)

        #         print(sub_cat_df.head())

        #     print(df.head())
        #     print(sub_unique)


        print("..........................................Done")

        final_df=pd.DataFrame({"Terminal_Id":atm_tamp,"Sub-Category":sub_cat_tamp,"Time After You Should Service":time_ser_tamp})

        # print(final_df)

        return  final_df


# op=aveg_time().avg_time_func("S1BB005080002")
#
#
# app=dash.Dash(__name__)
# app.layout=html.Div([html.P("Data_table"),
#                             html.Div(
#                               dash_table.DataTable(id='table',
#                                                    columns=[{"name":i,"id":i}for i in op.columns.to_list()],
#                                                    data=op.to_dict('records')))],style={'textAlign':'center'})
# if __name__ == '__main__':
#     app.run_server()