# from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2
from dash.dependencies import Input, Output
import plotly.graph_objects as go  # (need to pip install plotly==4.4.1)

# app1 = Flask(__name__)

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
df = []

try:
    connection = psycopg2.connect(user="candidato",
                                  password="crossnova20",
                                  host="178.22.68.101",
                                  port="5434",
                                  dbname="auto")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from auto"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from auto table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    df = mobile_records
    in8 = 0
    for row in mobile_records:
        x1.append(row[0])
        x2.append(row[1])
        x3.append(row[2])
        x4.append(row[3])
        x5.append(row[4])
        x6.append(row[5])
        x7.append(row[6])

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

fig = go.Figure()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Label(['Exercise 1']),
    ]),
    html.Div([
        dcc.Dropdown(
            id='xaxis',
            options=[
                {'label': '1 - acceleration', 'value': 1},
                {'label': '2 - cilinders', 'value': 2},
                {'label': '3 - displacement', 'value': 3},
                {'label': '4 - horsepower', 'value': 4},
                {'label': '5 - model_year', 'value': 5},
                {'label': '6 - weight', 'value': 6},
                {'label': '7 - mpg', 'value': 7}
            ],
            value=1,
            style={"width": "50%"}
        )
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(
            id='yaxis',
            options=[
                {'label': '1 - acceleration', 'value': 1},
                {'label': '2 - cilinders', 'value': 2},
                {'label': '3 - displacement', 'value': 3},
                {'label': '4 - horsepower', 'value': 4},
                {'label': '5 - model_year', 'value': 5},
                {'label': '6 - weight', 'value': 6},
                {'label': '7 - mpg', 'value': 7}
            ],
            value=2,
            style={"width": "50%"}
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

], style={'padding': 10})

@app.callback(
    Output('the_graph', 'figure'),
    [Input('xaxis', 'value'), Input('yaxis', 'value')]
)
def update_graph(xaxis_name, yaxis_name):
    xp = x1
    yp = x2
    xaxis_final_name = '1 - acceleration'
    yaxis_final_name = '2 - cilinders'
    if xaxis_name == 1:
        xp = x1
        xaxis_final_name = '1 - acceleration'
    elif xaxis_name == 2:
        xp = x2
        xaxis_final_name = '2 - cilinders'
    elif xaxis_name == 3:
        xp = x3
        xaxis_final_name = '3 - displacement'
    elif xaxis_name == 4:
        xp = x4
        xaxis_final_name = '4 - horsepower'
    elif xaxis_name == 5:
        xp = x5
        xaxis_final_name = '5 - model_year'
    elif xaxis_name == 6:
        xp = x6
        xaxis_final_name = '6 - weight'
    elif xaxis_name == 7:
        xp = x7
        xaxis_final_name = '7 - mpg'
    else:
        xp = x1
    if yaxis_name == 1:
        yp = x1
        xaxis_final_name = '1 - acceleration'
    elif yaxis_name == 2:
        yp = x2
        yaxis_final_name = '2 - cilinders'
    elif yaxis_name == 3:
        yp = x3
        yaxis_final_name = '3 - displacement'
    elif yaxis_name == 4:
        yp = x4
        yaxis_final_name = '4 - horsepower'
    elif yaxis_name == 5:
        yp = x5
        yaxis_final_name = '5 - model_year'
    elif yaxis_name == 6:
        yp = x6
        yaxis_final_name = '6 - weight'
    elif yaxis_name == 7:
        yp = x7
        yaxis_final_name = '7 - mpg'
    else:
        yp = x1
        yaxis_final_name = '2 - cilinders'

    return {'data': [go.Scatter(x=xp,
                                y=yp,
                                mode='markers',
                                text='',
                                marker={'size': 15,
                                        'opacity': 0.5,
                                        'line': {'width': 0.5, 'color': 'white'}})],
            'layout': go.Layout(title='Scatter Plot',
                                xaxis={
                                    'title': 'x: variable 1: ' + xaxis_final_name},
                                yaxis={
                                    'title': 'y: variable 2: ' + yaxis_final_name},
                                hovermode='closest')}

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5000)


# @app1.route('/') https://34.229.102.89:8050/  https://34.229.102.89:5000/