from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from . import (pieChart, genre_dropdown)

def create_layout(app,data):
    heading = html.H1(
        'Game Sales',
        className = 'bg-primary text-secondary p-2 mb-3'
    )
    return dbc.Container([
        dbc.Row([
            dbc.Col(heading)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(
                [
                    genre_dropdown.render(app,data), 
                   
                ],
                className="dropdown-container"
                ),lg= 6),
            dbc.Col(pieChart.render(app,data), lg =6),
        ]),
     ])