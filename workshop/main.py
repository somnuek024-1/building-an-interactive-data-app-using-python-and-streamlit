import pandas as pd
import streamlit as st


st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
st.write(df)

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"
df = pd.read_csv(url)
st.write(df)

number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")

import pandas as pd
import streamlit as st
import plotly.express as px


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"

df = pd.read_csv(url)
df_grouped_by_planet = df.groupby("year")["mass"].mean()
st.bar_chart(df_grouped_by_planet)

import plotly.express as px
import streamlit as st


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"

df = pd.read_csv(url)
df_grouped_by_planet = df.groupby("year")["mass"].mean()
st.bar_chart(df_grouped_by_planet)

# พลอตกราฟด้วย Plotly
fig = px.bar(df_grouped_by_planet.reset_index(), x="year", y="mass")
st.plotly_chart(fig)

with st.sidebar:
    st.write("This is a sidebar")
    option = st.selectbox(
        "Which number do you like best?",
        ["1", "2", "3", "4", "5"]
    )