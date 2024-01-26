
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
import json
import sys
import os

if __name__ == '__main__':

    # print current working dir
    print(os.getcwd())

    # Load JSON data
    with open('ai_topics.json', 'r') as f:
        data = json.load(f)

    # Convert JSON data to a DataFrame for easier processing
    df = pd.DataFrame(data)

    # Set up the Streamlit app
    st.subheader('Streamlit demo for Bachelor Thesis - OsloMet 2024')
    st.title('AI Topics and Number of Academic Papers')

    # Create a bar chart for each topic
    for topic in df['topic']:
        papers_per_year = df[df['topic'] == topic]['papers_per_year'].iloc[0]
        years = list(papers_per_year.keys())
        counts = list(papers_per_year.values())

        st.subheader(topic)
        fig, ax = plt.subplots()
        ax.bar(years, counts)
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Papers')
        st.pyplot(fig)

    sys.exit()
