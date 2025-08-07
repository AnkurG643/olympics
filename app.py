import streamlit as st
import pandas as pd
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv('data/athlete_events.csv')
region_df = pd.read_csv('data/noc_regions.csv')
df= preprocessor.preprocess(df, region_df)
st.sidebar.title('Olympics Analysis')

user_menu=st.sidebar.radio(
    'select an option',('Medal Tally','overall analysis','country-wise analysis','athlete-wise analysis')
)


if user_menu=='Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox('Select Year',years)
    selected_country=st.sidebar.selectbox('Select Country',country)
    medal_tally= helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title('Overall Medal Tally')
    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country + ' Overall Performance')
    if selected_year!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in ' + str(selected_year))
    if selected_year!='Overall' and selected_country!='Overall':
        st.title(selected_country + ' Performance in ' + str(selected_year))
    st.table(medal_tally)
if user_menu=='overall analysis':
    editions=df['Year'].unique().shape[0]-1
    sports=df['Sport'].unique().shape[0]
    cities=df['City'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]
    st.title('Top Statistics')
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Sports')
        st.title(sports)
    with col3:
        st.header('Host Cities')
        st.title(cities)
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)
    nations_over_time=helper.data_over_time(df,'region')
    fig=px.line(nations_over_time,x="Edition",y="region")
    st.title('Participation Over the Years')
    st.plotly_chart(fig)

    events_over_time=helper.data_over_time(df,'Event')
    fig=px.line(events_over_time,x="Edition",y="Event")
    st.title('Events Over the Years')
    st.plotly_chart(fig)

    athlete_over_time=helper.data_over_time(df,'Name')
    fig=px.line(athlete_over_time,x="Edition",y="Name")
    st.title('Athletes Over the Years')
    st.plotly_chart(fig)

    st.title("No. of Events Over Time(Every sport)")
    fig,ax=plt.subplots(figsize=(20,20))
    x=df.drop_duplicates(['Year','Sport','Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'overall')
    selected_sport=st.selectbox('Select a Sport',sport_list)
    x=helper.most_successful(df, selected_sport)
    st.table(x)