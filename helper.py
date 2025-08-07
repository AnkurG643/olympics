import numpy as np

def fetch_medal_tally(df, year, country):
    year = str(year).lower()
    country = str(country).lower()

    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    flag = 0

    if year == 'overall' and country == 'overall':
        temp_df = medal_df
    elif year == 'overall' and country != 'overall':
        flag = 1
        temp_df = medal_df[medal_df['region'].str.lower() == country]
    elif year != 'overall' and country == 'overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    else:
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'].str.lower() == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    return x


def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    medal_tally['Gold'] = medal_tally['Gold'].astype(int)
    medal_tally['Silver'] = medal_tally['Silver'].astype(int)
    medal_tally['Bronze'] = medal_tally['Bronze'].astype(int)
    medal_tally['Total'] = medal_tally['Total'].astype(int)
    return medal_tally

def country_year_list(df):
    years=df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')
    country=np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'Overall')
    return years,country

def data_over_time(df, col):
    temp_df = df.drop_duplicates(subset=['Year', col])
    data_over_time = temp_df.groupby('Year')[col].nunique().reset_index()
    data_over_time.rename(columns={'Year': 'Edition', col: f'{col}'}, inplace=True)
    return data_over_time

def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    # Get top 15 athletes by medal count
    top_athletes = temp_df['Name'].value_counts().reset_index()
    top_athletes.columns = ['Name', 'Medals']  # Rename columns properly

    # Merge with original df to get sport and region
    merged = top_athletes.head(15).merge(df, on='Name', how='left')[['Name', 'Medals', 'Sport', 'region']]
    merged = merged.drop_duplicates('Name')

    return merged
