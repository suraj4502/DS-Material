import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



df = pd.read_csv('vgsales.csv')
df['Publisher'].fillna("Unknown",inplace= True) 

# sidebar
st.sidebar.title("Sales Dashboard📊")
st.sidebar.markdown("---")
inp = st.sidebar.radio('Select',['Overview.',
        'Year wise Analyis.',
        'Genre wise Analysis.',
        'Platform wise Analysis.',
        'Publisher wise Analysis.'])

#Overview
if inp == 'Overview.':
    st.title("Video Games Sales Analysis...🎮")
    st.markdown("---")
    
    TS = df['Global_Sales'].sum()
    TG = df.shape[0]
    TP = len(df['Publisher'].unique())
    
    col1, col2 , col3 = st.columns([1,1,1])
    
    col1.metric("Total Sales",value=TS,delta="+")
    
    col2.metric("Total Games Released.",value=TG, delta="+")
    
    col3.metric("Total Publishers.",value=TP, delta="+")
    
    st.markdown("---")
    
    st.image('img.jpg')
    
    st.header("Data exploration.")
    
    st.markdown("""
        
    ---        
    #### *※ Columns in the data along with their description.*

    - `Rank:` The ranking position of the game in terms of global sales.
    - `Name:` The name of the video game.
    - `Platform:` The gaming platform (console or system) on which the game was released.
    - `Year:` The year when the game was released.
    - `Genre:` The genre or category of the game (e.g., action, adventure, sports).
    - `Publisher:` The company or entity responsible for publishing and distributing the game.
    - `NA_Sales:` Sales of the game in North America (in millions of units).
    - `EU_Sales:` Sales of the game in Europe (in millions of units).
    - `JP_Sales:` Sales of the game in Japan (in millions of units).
    - `Other_Sales:` Sales of the game in regions other than North America, Europe, and Japan (in millions of units).
    - `Global_Sales:` Total global sales of the game (sum of sales across all regions, in millions of units).
    ---
            """)
    
    st.header("Data.")
    st.dataframe(df)
    
    st.sidebar.markdown("---")
    game = st.sidebar.selectbox("Select a Game to view its information",options=df.Name.unique())
    gbutton = st.sidebar.button("Press to show info.")
    
    
    st.markdown("---")
    st.header(f"Info of {game}.")
    if gbutton:
            st.write(df[df['Name'] == game])
            
            
# 'Year wise Analyis.'
elif inp == 'Year wise Analyis.':
        
        st.title("Year wise analysis📅")
        
        
        st.header("Year wise Sales.")
        fig = px.line(df.groupby('Year')['Global_Sales'].sum().reset_index(), x='Year', y='Global_Sales')
        st.plotly_chart(fig)
        
        
        st.header("Number of Games Released Over Time.")
        games_released_over_time = (df.groupby('Year')['Name'].count().reset_index()).rename(columns = {'Name':'count'})
        fig = px.bar(games_released_over_time, x='Year', y='count',text_auto=True,
                color_discrete_sequence=['#FCAEAE']) 
        st.plotly_chart(fig)
        


#Genre wise Analysis.
elif inp == 'Genre wise Analysis.':
        st.title('Genre wise Analysis🧿')
        
        # top genres based on GLoabal Sales
        st.header("Gloabal Sales in each genre.")
        temp = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending = False)
        fig = px.bar(temp, x = temp.index,y = temp)
        st.plotly_chart(fig)
        
        temp = temp.reset_index()
        st.header("Contribution of each genre in sales.")
        fig = px.pie(temp,values = 'Global_Sales' , names = 'Genre')
        st.plotly_chart(fig)
        
elif inp == 'Platform wise Analysis.':
        st.title("Platform wise analasis")
        
        st.subheader('Top platforms based on sales.')
        temp = (df.groupby('Platform')['Global_Sales'].sum()
                .sort_values(ascending = False).reset_index().head(10))
        fig =px.bar(temp,x='Platform',y= 'Global_Sales')
        st.plotly_chart(fig)
        
        
elif inp == 'Publisher wise Analysis.':
        st.title("Publisher wise Analysis.")
        
        st.header("Top 10 publishers by sales.")
        temp = (df.groupby("Publisher")['Global_Sales'].sum()
                .reset_index()
                .sort_values("Global_Sales",ascending= False)
                .head(10))
        
        fig =px.bar(temp,x = 'Publisher',y= 'Global_Sales')
        st.plotly_chart(fig)
        
        
        st.subheader("Contriution in Sales.")
        fig = px.pie(temp,values='Global_Sales',names= 'Publisher')
        st.plotly_chart(fig)
        
        st.subheader("Running Bar chart , Publisher and Sales.")
        df1=df[df['Publisher'].isin(temp.Publisher.unique())]
        fig =px.bar(df1, x='Publisher',y = 'Global_Sales',animation_frame='Year',animation_group='Publisher',range_y=[0,60])
        st.plotly_chart(fig)
        