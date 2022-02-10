import dash
import dash_cytoscape as cyto
from dash import html
import cylo_formatter as cylo
from dash.dependencies import Input, Output
import json
my_dataset = "test.mtx"

GRAPH = cylo.create_elements(dataset=my_dataset)


app = dash.Dash(__name__)

app.layout = html.Div([
        html.Div([
            html.H1('Amazon Co-purchased Products Network Analysis')
        ]),
        html.Div([
            html.Div([
            cyto.Cytoscape(
                    id='cytoscape-two-nodes',
                    layout={'name': 'cose'},
                    style={'width': '100%','height': '80vh',
                           'background': '#5E8EF0'},
                    elements=GRAPH,
                   stylesheet=[
                        {
                            'selector' : 'node',
                            'style':{'content' : 'data(label)',
                                     'background-color' : 'red'
                                    }
                        },
                        {
                            'selector' : 'edge',
                            'style':{
                                     'line-color' : 'black'
                                    }
                        }
                    ]



                )], style={'flex': '3','right-margin':'5px','border-radius':'15px','overflow':'hidden'})
    ,
        html.Div([
                html.Div([

                    html.H1('Node id input:'),
                    html.Div([
                        html.P('Node Id :',id='cytoscape-tapNodeData-output'),
                        html.P("Number of connections : "),
                        html.P('Community id:')
                    ])
                ],className='right-containers',style={'flex':'1','background-color':'#5E8EF0','border-radius':'15px','margin-bottom':'10px'}),
                html.Div([

                    html.H1('Hello Dash'),
                    html.Div([
                        html.P('Dash converts Python classes into HTML'),
                        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end"),
                    ])
                ],className='right-containers',style={'flex':'1','background-color':'#5E8EF0','border-radius':'10px'})
    ],style={'display':'flex','flex-direction':'column','flex':'2','margin-left':'10px'})
        ], style={'display': 'flex','position':'relative','top':'20px','height':'80vh'})],className='container-div',style={'color':'white','height':'100vh','padding':'10px 10px'})

@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape-two-nodes', 'tapNodeData'))
def displayTapNodeData(data):
    if data:

        return "Node Id: " + data['id']



if __name__ == '__main__':

    app.run_server(debug=True)







