#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.express as px
import streamlit as st
import pandas as pd
import json


@st.cache_data
def load_data():
    try:
        df = pd.read_json('ai_topics.json')
        return df
    except FileNotFoundError:
        st.error("The file 'ai_topics.json' was not found.")
        return pd.DataFrame()
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return pd.DataFrame()


if __name__ == '__main__':
    df = load_data()

    # Set up the Streamlit app layout
    st.sidebar.title('Bachelor Thesis Project')
    st.sidebar.subheader('OsloMet 2024')
    st.sidebar.title('AI Topics Explorer')

    # Navigation
    page = st.sidebar.radio('Select a Page', ['Home', 'Detailed View', 'About'])

    if page == 'Home':
        st.title('AI Topics Overview')
        st.markdown("""
            <p style='font-size: 1.5em;'>
            Welcome to AI Taxonomy Explorer! <br>
            This tool visualizes the trends in AI research over recent years, based on the number of academic papers 
            published in various AI subfields.
            </p>
            """, unsafe_allow_html=True)

        st.image('ai-taxo-colour.jpg', caption='AI Research Visualization')  # Replace with the path to your image

        st.subheader('Summary of Data')
        total_papers = df.drop(columns=['topic']).sum().sum()  # Sum of all papers
        st.markdown(f"""
        - **Total Number of Papers Analyzed:** `{total_papers}`
        """)

        # You can add more statistics here based on your data

        st.subheader('Distribution of Papers Across AI Topics')
        topic_distribution = df.melt(id_vars=['topic'], var_name='Year', value_name='Count').groupby('topic')[
            'Count'].sum()
        fig = px.bar(topic_distribution, x=topic_distribution.index, y='Count', labels={'Count': 'Number of Papers'},
                     title='Total Papers per AI Topic')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader('Trend of AI Research Over the Years')
        yearly_trend = df.drop(columns=['topic']).sum()
        fig = px.line(yearly_trend, x=yearly_trend.index, y=yearly_trend.values,
                      labels={'y': 'Number of Papers', 'index': 'Year'}, title='Trend of AI Research Over the Years')
        st.plotly_chart(fig, use_container_width=True)

    elif page == 'Detailed View':
        st.title('AI Topics on arXiv')

        # Dropdown to select topic
        topic = st.selectbox('Select Topic', df['topic'].unique())

        # Slider for selecting the range of years
        years = [col for col in df.columns if col.isdigit()]  # This will collect only the year columns
        min_year, max_year = int(min(years)), int(max(years))
        year_range = st.slider('Select the year range', min_year, max_year, (min_year, max_year))

        # Filter data based on selection
        topic_data = df[df['topic'] == topic]
        topic_data = topic_data.melt(id_vars=['topic'], value_vars=years, var_name='Year', value_name='Count')
        topic_data = topic_data[
            (topic_data['Year'].astype(int) >= year_range[0]) & (topic_data['Year'].astype(int) <= year_range[1])]

        # Interactive chart with Plotly
        fig = px.bar(topic_data, x='Year', y='Count', labels={'Count': 'Number of Papers'},
                     title=f'Number of Papers for {topic}')

        st.plotly_chart(fig, use_container_width=True)

    elif page == 'About':
        st.title('About the Project')
        st.markdown("""
            <p style='font-size: 1.5em;'>
            This project is part of a bachelor thesis at OsloMet 2024. <br>
            It aims to provide a dynamic visualization 
            tool to explore the ever-expanding field of artificial intelligence.</p>
            """, unsafe_allow_html=True)
