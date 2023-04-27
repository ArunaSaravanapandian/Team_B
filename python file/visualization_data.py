import pandas as pd
import plotly.express as px


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

    # dataframe for health
    health_data = dataframes_list[1]

    print("start school")

    # map visualization for schools in Kenya
    fig1 = px.scatter_mapbox(
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
    fig1.show()
    print("end")

    # map visualization for healthcare facilities in Kenya
    print("start health")
    fig2 = px.scatter_mapbox(
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
    fig2.show()
    print("end")



