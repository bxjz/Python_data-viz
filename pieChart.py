import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from .ids import *


def render(app,data):
    @app.callback(
        Output(PIE_CHART, "children"),
        [
            Input(GENRE_DROPDOWN, "value"),
            
        ]
    )
    def update_pie_chart(genre):
        print(data)
        filtered_data = data.query(
            "genre in @genre"
        )
        if filtered_data.shape[0] == 0:
            return html.Div("No data is selected", id=PIE_CHART)

        fig = px.pie(filtered_data, values="total_sales", names="genre",hole = 0.4)
        return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)
    return html.Div(id=PIE_CHART)