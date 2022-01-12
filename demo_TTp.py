import dash
from dash import html
from dash import dcc
# from dash import dash_core_components as dcc
# import dash import dcc
# import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')
import datetime as dt
import numpy as np


#
import plotly.express as px
from plotly.subplots import make_subplots

class graphs():
    def garaph_funce(self,df):

        df['Tic_Rais_date_time'] = pd.to_datetime(df['Tic_Rais_date_time'])
        df['months'] = df.Tic_Rais_date_time.apply(lambda x: dt.datetime.strftime(x, '%b %Y')).tolist()
        df = df.set_index('Tic_Rais_date_time')
        df.sort_index(inplace=True)
        print(df.columns)


        year_sub_df=pd.DataFrame(df['Sub_Category'].value_counts())
        year_sub_df['subs']=year_sub_df.index
        year_sub_df.reset_index(drop=True,inplace=True)
        year_sub_df.columns=['Counts','Sub_Category']
        #
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{"type": "pie"}, {"type": "bar"}]],
        subplot_titles=(f"Yearly {df['Terminal_ID'][0]} pie", f"Yearly {df['Terminal_ID'][0]} Bar",) )

        fig.add_trace(go.Pie(labels=year_sub_df['Sub_Category'], values=year_sub_df['Counts'], name="Yearly Sub_category"),
                      1, 1)

        fig.add_trace(go.Bar(x=year_sub_df['Sub_Category'],y=year_sub_df['Counts']
                                 ,marker_color=['rgb(99, 110, 250)','rgb(239, 85, 59)','rgb(0, 204, 150)',
                                            'rgb(171, 99, 250)','rgba(255,161,90,255)','rgba(140,233,249,255)',
                                            'rgba(255,102,146,255)','rgba(182,232,128,255)','rgba(255,151,255,255)',
                                            'rgba(254,203,82,255)','rgba(198,202,253,255)'],text=year_sub_df['Counts']),1,2)


        # fig.add_trace(go.Bar(x=year_sub_df['Sub_Category'],y=year_sub_df['Counts']),1,2)
        fig.update_layout({"plot_bgcolor": "rgba(235, 254, 255, 0.8)", "paper_bgcolor": "rgba(215, 253, 255, 0.8)", })
        return fig



#
# sdf=pd.read_csv('Excel_sheets/S1BB005080002.csv')
# print()
# gp=graphs().garaph_funce(sdf)
# print(gp)
# rgb()

