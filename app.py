#here are full codee
import pandas as pd
# import flask
from dash import html
from dash.dependencies import State
# import dash_bootstrap_components as dbc
from dash import dcc
from demo_TTp import *
from sub_cate_reange_month import *
from average_time_service import *
import matplotlib
import seaborn

# figures_graphs=graphs().garaph_funce()


tamp_atm_name=[]
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['https://codepen.io/hynes-dialpad/pen/vYmvwPe']


# app_flask = flask.Flask(__name__)
# app_dash = dash.Dash(__name__, server=app_flask, url_base_pathname='/atm_service_analysis/')
app_dash = dash.Dash(__name__,suppress_callback_exceptions=True)
server=app_dash.server

app_dash.layout = html.Div([
    html.Div([
    html.H1('ATM Service Analysis',style={'textAlign':'center',"background-color":"#0ec7ae","border":"1px solid blue"})],style={"background-color":"rgba(215, 253, 255, 0.8)",}), #"width":"30%" 'textAlign':'left','padding-left': '450px'

    html.Div([
    dcc.Input(id='username', value='Enter ATM Name', type='text',style={'textAlign':'center','width':"200px","height":"30px","background-color":"rgba(235, 254, 255, 0.8)","font-size":"15px","border":"1px solid blue"}),
    html.Button(id='submit-button', type='submit', children='Submit',style={"margin-left": "10px",'width':"70px","height":"35px","background-color":"#0ec7ae","border":"1px solid blue"})],style={'textAlign':'center'}),
    html.Div(id='output_div',style={"background-color":"rgba(215, 253, 255, 0.8)"}),
    html.Br(),
    html.Div(id="input_output",style={"background-color":"rgba(215, 253, 255, 0.8)"}),
                    ],style={"background-color":"rgba(215, 253, 255, 0.8)","border": "1px solid black"})
#


@app_dash.callback(
              Output('output_div', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('username', 'value')])

def update_output(clicks, input_value):

    tamp_atm_name.append(input_value)

    if input_value!="Enter ATM Name":
        op = aveg_time().avg_time_func(input_value)


    if len(input_value) ==0:



        return html.Div([

                            dcc.ConfirmDialog(
                                id='confirm-dialog',
                                displayed=True,
                                message='Please Enter Your ATM Name '
                            )])

    if clicks is not None and input_value !='Enter ATM Name':

        sdf = pd.read_csv(f'Atm_saprated_data//{input_value}.csv')





        figures_graphs = graphs().garaph_funce(sdf)
        sub_monthlydf = reng_subs().reng_sbs_func(sdf)



        unique_subs = sub_monthlydf.columns.tolist()
        unique_subs.insert(0, "All Sub-Category")


        return html.Div([

                dcc.ConfirmDialog(
                    id='confirm-dialog',
                    displayed=True,
                    message=f'Your ATM Name {input_value}',
                ),

                html.Br(),

                #Creat your graphs here   ------------------------------------------------
                html.Div(
                dcc.Graph(
                    figure =figures_graphs
                    ,style={"width":"1200px","height":"400px","border":"1px solid blue"}),style={'padding-left':'70px'}),

                html.Div([
                        html.Div([
                                 html.Div([
                                  html.P("Month wise- Subcategory",style={"background-color":"#0ec7ae","width":"250px","height":"30px","font-size":"20px","border":"1px solid blue"}),
                                  dcc.Dropdown(id='dropdown1',
                                                    # options=[{'label':'one','value':'one'},
                                                    #          {'label':'two','value':'two'}],
                                                    options=[{'label':i,'value':i}for i in unique_subs],

                                                    placeholder='Please select Sub-Category',
                                                    value='Dishh',style={'width': '200px','font-size':'15px','padding-left': '20px',"background-color":"rgba(235, 254, 255, 0.8)"})],style={'width': '20%','display': 'inline-block','textAlign':'center'})],style={'textAlign':'center'}),
                                  html.Br(),


                                  html.Div(dcc.Graph(id='graph1',
                                                 className='barograph',
                                                 style={'width': '1200px', 'height': '600px','textAlign':"center","border":"1px solid blue"} #,"border":"1px solid blue"
                                                 ),
                                       style={'display': 'inline-block','padding-left':'70px'}),

                                  html.Div([html.P(f"Predicting Time when subcategory error can happen {input_value}",style={'textAlign':'center'}),
                                                          html.Div([
                                                            dash_table.DataTable(id='table',
                                                                                 columns=[{"name":i,"id":i}for i in op.columns.to_list()],
                                                                                 data=op.to_dict('records'),

                                                                                 style_header={
                                                                                     'backgroundColor': 'rgba(0, 195, 169, 0.8)',
                                                                                     'color': 'black',
                                                                                     'border': '2px solid blue'
                                                                                 },
                                                                                 style_data={
                                                                                     'backgroundColor': 'rgba(235, 254, 255, 0.8)',
                                                                                     'color': 'black',
                                                                                     'border': '1px solid black'
                                                                                 },
                                                                                 style_table={"width":"700px",'text-align': 'left', 'padding-left': '290px'},
                                                                                 # fill_width=False
                                                                                 )])])




                      ])])



                #enndd---------------------------------------------------------------



    if clicks is not None and input_value =='Enter ATM Name':


        return html.Div([

                            dcc.ConfirmDialog(
                                id='confirm-dialog',
                                displayed=True,
                                message='Please Enter Your ATM Name ',
                            )])


@app_dash.callback(
Output('graph1', 'figure'),
[Input('dropdown1', 'value')]
)

def update_graphvalue2(value):
    # print(f"==================={value}")
    # fig=None
    # global fig
    fig=""

    atm_name_var=tamp_atm_name[-1]
    # print(atm_name_var)
    sdf2=pd.read_csv(f'Atm_saprated_data\\{atm_name_var}.csv')

    # print("====================================================")
    # print(sdf2['Terminal_ID'])
    sub_monthlydf = reng_subs().reng_sbs_func(sdf2)

    if value == "All Sub-Category":
        fig = make_subplots(rows=2, cols=1)
        for i in sub_monthlydf.columns.tolist():
            # print(i)
            fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[i], text=sub_monthlydf[i], name=str(i), ),
                          1, 1)
            fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[i],
                                     mode='lines',
                                     name=str(i), ),
                          2, 1)

            fig.update_layout({"plot_bgcolor": "rgba(235, 254, 255, 0.8)", "paper_bgcolor": "rgba(215, 253, 255, 0.8)"})



    else:
        fig = make_subplots(rows=2, cols=2, specs=[[{}, {}],
                                                   [{"colspan": 2}, None]],
                            subplot_titles=(
                            f"Month wise {value} Bar", f"Month wise {value} Line", f"Month wise {value}  Bar-line"))
        fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[value], text=sub_monthlydf[value], name=value, ),
                      1, 1)

        fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[value],
                                 mode='lines',
                                 name=value, ),
                      1, 2)

        fig.add_trace(go.Bar(x=sub_monthlydf.index, y=sub_monthlydf[value], name=value, ),
                      2, 1)

        fig.add_trace(go.Scatter(x=sub_monthlydf.index, y=sub_monthlydf[value],
                                 mode='lines',
                                 name=value, ),
                      2, 1)

        fig.update_layout({"plot_bgcolor": "rgba(235, 254, 255, 0.8)", "paper_bgcolor": "rgba(215, 253, 255, 0.8)"})

    return fig
#
# @app_flask.route('/')
# def home():
#     return '/atm_service_analysis/ on url'
#
#
# @app_flask.route('/plotly_dashboard')
# def render_dashboard():
#     return flask.redirect('/atm_service_analysis/')

# Append an externally hosted CSS stylesheet



# print(tamp_atm_name)
if __name__ == '__main__':
    app_dash.run_server(debug=False)




