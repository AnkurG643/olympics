import streamlit as st
import pandas as pd
import preprocessor,helper
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