from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


def render(app,data):
    all_genres = data['genre'].unique()

    @app.callback(
        Output(GENRE_DROPDOWN, "value"),
        Input(SELECT_ALL_GENRES, "n_clicks")
    )
    def select_all_genres(n):
        return all_genres

    dropdown = html.Div(
        [
            html.H6("Genre"),
            dcc.Dropdown(
                id=GENRE_DROPDOWN,
                options=[{"label":genre, "value":genre} for genre in all_genres],
                multi=True,
            ),
            html.Button(
                id=SELECT_ALL_GENRES,
                children=["Select All"],
                className="dropdown-button",
                n_clicks=0
                ),
        ]
    )
    return dropdown
