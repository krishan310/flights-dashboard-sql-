import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from dbhelper import DB
import plotly.figure_factory as ff

db = DB()
st.sidebar.title('Flights Analytics')
user_option= st.sidebar.selectbox('Menu' , ['select one' , 'Check flights' , 'Analytics'])
if user_option=='Check flights':
    st.title('Check flights')
    col1 , col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)
elif user_option=='Analytics':
    airline , frequency = db.fetch_airline_frequency()

    # import plotly.graph_objects as go

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo='label+percent',
            textinfo='value'
        )
    )

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()

    fig = px.bar(x=city, y=frequency1, labels={'x': 'City', 'y': 'Frequency'})
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    fig = px.line(x=date, y=frequency2, labels={'x': 'date', 'y': 'frequency'})
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    st.title('Tell about the project ')

