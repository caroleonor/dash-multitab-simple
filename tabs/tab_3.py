import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('How much have you applied the knowledge in the past 3 months?'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Slider(
                id='page-3-slider',
                min=0,
                max=100,
                step=10,
                marks={i:str(i) for i in range(0, 101)},
                value=50,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
