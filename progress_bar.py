import streamlit as st
import time

# progress bar
bar_p = st.progress(0)
for percentage_complete in range(100):
    time.sleep(.01)
    bar_p.progress(percentage_complete+1)

# Status message
# display a temporary message when executing a block of code

with st.spinner('Please wait'):
    time.sleep(3)
st.text("Complete!")

