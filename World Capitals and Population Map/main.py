import plotly.express as px
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

data1 = pd.read_csv('capitals.csv', encoding='ISO-8859-1')
data2 = pd.read_csv('populations.csv', encoding='ISO-8859-1')

merged_data = pd.merge(data1, data2, on='Country', how='inner')
country_column = "Country" 
capital_column = "Capital"  
population_column = "Population"
continent_column="Continent"  
land_area_column="Land Area"
urban_population_column="Urban Pop"

fig = px.choropleth(
    merged_data,
    locations=country_column,
    locationmode="country names",
    color=country_column,
    hover_data=[capital_column, population_column],  
    color_continuous_scale=px.colors.sequential.Plasma,
    title="World Capitals and Population Map"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='world-map',
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '80vh'}
    ),
    html.Div(
        id='country-info',
        style={'fontSize': 18, 'padding': '10px','font-family':'Arial, sans-serif','font-weight':'bold'} 
    )
])

@app.callback(
    Output('country-info', 'children'),
    Input('world-map', 'hoverData')
)

def display_country_info(hoverData):
    if hoverData:
        selected_country = hoverData['points'][0]['location']
        selected_country_data = merged_data[merged_data[country_column] == selected_country]
        country_info = [
            html.P(f"COUNTRY : {selected_country}"),
            html.P(f"CAPITAL : {selected_country_data[capital_column].values[0]}"),
            html.P(f"POPULATION : {selected_country_data[population_column].values[0]}"),
            html.P(f"CONTINENT : {selected_country_data[continent_column].values[0]}"),
            html.P(f"LAND AREA (KM²) : {selected_country_data[land_area_column].values[0]}"),
            html.P(f"URBAN POPULATION : {selected_country_data[urban_population_column].values[0]}")
        ]
        return country_info
    return None

if __name__ == '__main__':
    app.run_server(debug=True)