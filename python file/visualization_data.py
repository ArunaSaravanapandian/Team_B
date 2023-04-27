import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def visualize_data():
    # assign dataset names
    list_of_names = ['school', 'health']

    # create empty list
    dataframes_list = []

    # append datasets into the list
    for i in range(len(list_of_names)):
        temp_df = pd.read_csv("./csv/" + list_of_names[i] + ".csv")
        dataframes_list.append(temp_df)

    # dataframe for school
    school_data = dataframes_list[0]
    school_dataframe = pd.DataFrame(school_data)

    # finding the number of schools in each county
    school_county = school_dataframe.pivot_table(index=['County'], aggfunc='size')

    # dataframe for health
    health_data = dataframes_list[1]
    health_dataframe = pd.DataFrame(health_data)

    # finding the number of schools in each county
    health_county = health_dataframe.pivot_table(index=['county'], aggfunc='size')

    # histogram of school and health data corresponding to the county
    histogram_visualization = go.Figure().add_trace(
        go.Histogram(
            x=health_data['county'],
            y=school_county,
            name="school"
        )
    ).add_trace(
        go.Histogram(
            x=health_data['county'],
            y=health_county,
            name="health"
        )
    ).update_layout(
        xaxis_title="County",
        yaxis_title="Number of county"
    )
    histogram_visualization.show()

    # map visualization for schools in Kenya
    map_school_visualization = px.scatter_mapbox(
        school_data,
        lat="Y_Coord",
        lon="X_Coord",
        hover_data=["SCHOOL_NAM"],
        color_discrete_sequence=["Blue"],
        opacity=0.5,
        zoom=5.5,
        height=700
    ).update_layout(
        mapbox_style="open-street-map",
        margin={"r": 100, "t": 5, "l": 3, "b": 26}
    )
    map_school_visualization.show()

    # map visualization for healthcare facilities in Kenya

    map_health_visualization = px.scatter_mapbox(
        health_data,
        lat="Latitude",
        lon="Longitude",
        hover_data=["FACILITY_N"],
        color_discrete_sequence=["Green"],
        opacity=0.5,
        zoom=5.5,
        height=700
    ).update_layout(
        mapbox_style="open-street-map",
        margin={"r": 100, "t": 5, "l": 3, "b": 26}
    )
    map_health_visualization.show()
