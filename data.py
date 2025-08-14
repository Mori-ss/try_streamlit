import streamlit as st
import pandas as pd

# students and marks
students = ['Milla Khalifa', 'Mark Ruffalo', 'Peter Zen', 'North Kim']
marks = [82, 76, 96,64]

# Creating df
df = pd.DataFrame()
df["Students name"] = students
df["Marks"] = marks

st.title("About students")
# display dataframe
st.dataframe(df)

#static table
st.table(df)

# metrics
st.metric("KPI", 56, 3)

# json
st.json(df.to_dict())