from dash import Dash
import dash_bootstrap_components as dbc 
from components.layout import create_layout
from data.util import get_data
import os

cwd = os.getcwd()
file_path = (f'{cwd}/data/finaldata.csv')

def main():
    data = get_data(file_path)
    app = Dash(external_stylesheets=[dbc.themes.COSMO])
    server = app.server
    app.title = 'Game Sales'
    app.layout = create_layout(app, data)
    app.run_server(debug=True)


if __name__ == '__main__':
    main()