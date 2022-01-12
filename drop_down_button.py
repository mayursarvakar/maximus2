# import yfinance as yf
import datetime as dt

import dash
import dash_core_components as dcc
# from dash import dash_core_components as dcc
# import dash import dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import warnings

import sub_cate_reange_month

warnings.filterwarnings('ignore')
import datetime as dt
import numpy as np
from plotly.subplots import make_subplots
from plotly.offline import iplot

from sub_cate_reange_month import *

df=pd.read_csv('S1BB005080002.csv')
#
sub_monthlydf=reng_subs().reng_sbs_func(df)
unique_subs=sub_monthlydf.columns.tolist()
unique_subs.insert(0,"All Sub-Category")
#
#
#
app=dash.Dash()
# fig = go.Figure()
app.layout = html.Div([html.H1("Heeeello"),
                     html.Div([
                     html.Div(dcc.Dropdown(id='dropdown1',
                                           # options=[{'label':'one','value':'one'},
                                           #          {'label':'two','value':'two'}],
                                           options=[{'label':i,'value':i}for i in unique_subs],

                                           placeholder='Please select Sub-Category',
                                           value='Dishh'),style={'width': '90%', 'display': 'inline-block'}
                                    ),
                     html.Div(dcc.Graph(id='graph1',
                                        className='barograph',
                                        style={'width': '1300px', 'height': '800px'}
                                        ),
                                        style={'display':'inline-block'})
                     ]
                         , style={'width': '41%', 'display': 'inline-block'})])

@app.callback(
Output('graph1', 'figure'),
[Input('dropdown1', 'value')]
)
def update_graphvalue2(value):
   # print(f"==================={value}")


   for i in sub_monthlydf.columns.tolist():
       if value==i:
           fig = make_subplots(rows=2, cols=2, specs=[[{}, {}],
                                                      [{"colspan": 2}, None]],
                               subplot_titles=(f"Month wise {i} Bar", f"Month wise {i} Line", f"Month wise {i}  Bar-line"))
           fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[i],text=sub_monthlydf[i],name=i,),
                         1, 1)

           fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[i],
                                    mode='lines',
                                    name=i,),
                         1, 2)

           fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[i],name=i, ),
                         2, 1)

           fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[i],
                                    mode='lines',
                                    name=i,),
                         2, 1)

   if value=="All Sub-Category":
           fig = make_subplots(rows=2, cols=1)
           for i in sub_monthlydf.columns.tolist():
               # print(i)
               fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[i], text=sub_monthlydf[i],name=str(i), ),
                             1, 1)
               fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[i],
                                        mode='lines',
                                        name=str(i), ),
                             2, 1)





   return fig


if __name__ == "__main__":
    app.run_server()