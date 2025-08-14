

import streamlit as st

#Title
st.title("Document Title")

# Header
st.header("Article Header", anchor=None)

# Subheader
st.subheader("Article subheader")

# Text
st.text("This is a text!")

# Markdown
st.markdown("Streamlit is **_very_ cool**.")

# Code
st.code("y =  mx + c")

#Code (specify language)
code = '''
def cal_avrg(numbers):
    sum_number = 0
    for i in numbers:
        sum_number += i
    average = sum_number / len(numbers)
        
    return average
        '''
st.code(code, language='python')

# Latex for add formulas
st.latex("\ int a y^2 \, dy")