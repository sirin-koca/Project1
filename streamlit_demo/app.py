#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.express as px
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="AI Taxonomy Explorer", page_icon="🕹️", layout="wide", initial_sidebar_state="expanded")


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
    st.sidebar.subheader('Streamlit demo by Sirin')
    st.sidebar.title('Bachelor Thesis Project')
    st.sidebar.subheader('OsloMet // SINTEF')
    st.sidebar.title('AI Topic Explorer')

    # Navigation
    page = st.sidebar.radio('Select a Page', ['Home', 'Detailed View', 'About'])

    # Search bar
    search_query = st.sidebar.text_input('Search', '')

    if search_query:
        # Assuming 'df' is your DataFrame and 'topic' is the column with text to search
        try:
            # Case-insensitive search
            filtered_data = df[df['topic'].str.contains(search_query, case=False, na=False)]
            st.sidebar.write(f"You searched for: {search_query}")
            st.write(filtered_data)
        except KeyError:
            st.error("The specified column does not exist in the DataFrame.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    if page == 'Home':
        st.title('Overview')
        st.markdown("""
            <p style='font-size: 1.5em;'>
            Welcome to AI Topic Explorer! <br><br>
            Navigate AI Research Trends with Ease. Discover the latest trends in AI research through a 
            straightforward and intuitive visual tool. <br> 
            Perfect for researchers and AI professionals, it offers a clear view of the most impactful topics 
            and their development over the years. <br>
            Simple yet powerful - get the insights you need to stay informed and connected with the AI community.
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
            AI Topics Explorer: A proof-of-concept visualization tool<br><br>
            As part of the bachelor thesis at OsloMet, this project unfolds an exploratory journey into the dynamic 
            world of artificial intelligence (AI). Developed in collaboration with SINTEF and Ontotext, the 
            AI Topics Explorer stands as a proof-of-concept (POC) that shows the potential of interactive 
            visualization to illuminate AI research trends.
            The tool encapsulates a digital prototype designed to map the spread of AI topics over time. 
            This initiative not only demonstrates the practical application of theoretical knowledge but serves as 
            a basic prototype for subsequent, more detailed development.<br>
            </p>
            """, unsafe_allow_html=True)
