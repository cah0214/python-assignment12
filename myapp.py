from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load dataset (built-in)
df = px.data.gapminder()

# Unique countries for dropdown
countries = df["country"].drop_duplicates().sort_values()

app = Dash(__name__)
server = app.server  # for deployment

app.layout = html.Div(
    [
        html.H1("GDP per Capita Growth"),
        html.P("Select a country to view GDP per capita over time (Gapminder dataset)."),

        dcc.Dropdown(
            id="country-dropdown",
            options=[{"label": c, "value": c} for c in countries],
            value="Canada",  # initial value
            clearable=False
        ),

        dcc.Graph(id="gdp-growth"),
    ],
    style={"maxWidth": "900px", "margin": "40px auto"}
)

@app.callback(
    Output("gdp-growth", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(country_name):
    filtered = df[df["country"] == country_name]

    fig = px.line(
        filtered,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Over Time: {country_name}",
        markers=True
    )

    fig.update_layout(xaxis_title="Year", yaxis_title="GDP per Capita")
    return fig

if __name__ == "__main__":
    app.run(debug=True)# dash app
