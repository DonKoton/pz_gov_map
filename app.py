import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="pz_gov_app")


def prepare_data():
    df = pd.read_excel("pz_gov.xlsm")

    df['fullAddress'] = df['Address'].str.cat(df[['City', 'Country']].values, sep=', ')

    df[['lat', 'lon']] = df.fullAddress.apply(geolocator.geocode).dropna().\
        apply(lambda x: pd.Series([x.latitude, x.longitude], index=['lat', 'lon']))

    return df


def plot_map_pz(mapbox_style):
    fig = px.scatter_mapbox(data_frame=prepare_data(),
                            lat='lat',
                            lon='lon',
                            hover_name='Name',
                            hover_data=['Address', 'City'],
                            zoom=10,
                            )

    fig.update_layout(mapbox_style=mapbox_style,
                      margin={'r': 10, 't': 10, 'l': 10, 'b': 10})
    fig.show()


plot_map_pz('open-street-map')
