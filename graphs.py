import pandas as pd
import plotly.express as px


# read csv
df=pd.read_csv('datafile.csv')

# filter data for Urban area and remove row of 'India'
# only select 'State/UT','Ever tobacco users (%)' columns
df_urban=df.loc[(df['Area']=='Urban') & (df['State/UT']!='India'),['State/UT','Ever tobacco users (%)']]


# setup bar chart
fig=px.bar(df_urban,x='State/UT',y='Ever tobacco users (%)',title='Ever Tobacco Users Per State (Urban)',color='State/UT',hover_name='State/UT')

# display chart
fig.show()