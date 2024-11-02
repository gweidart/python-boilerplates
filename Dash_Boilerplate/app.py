import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Welcome to Dash!"),
    html.P("This is a basic Dash application."),
    dcc.Input(id='input-text', type='text', placeholder='Enter text here'),
    html.Div(id='output-text')
])

# Define callback to update output
@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_output(value):
    if value:
        return f'You entered: {value}'
    return 'Enter something in the input box.'

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
