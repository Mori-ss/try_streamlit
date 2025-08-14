import streamlit as st
# Title for app
st.title('Body mass index(BMT) Calculator')

# READ THE WEIGHT
weight = st.number_input("Enter your weight(in kilograms)")

# READ THE HEIGHT
# use radio button to specify the units of measurement
status = st.radio("Specify the height measurement units: ", ('cm', 'm', 'feet'))

# Comparing different statuses for height measurement units
if status == 'cm':
    height = st.number_input('centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text('Enter your height')
if status == 'm':
    height = st.number_input('meters')
    try:
        bmi = weight / (height **2)
    except:
        st.text('Enter your height')
if status == 'feet':
    height = st.number_input('feet')
    # 1 meter = 3.28
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except:
        st.text('Enter your height')

# Check if the button has been pressed
if(st.button('Calculate the BMI')):
    # Print the bmi value
    st.text(f'Your BMI equal to {bmi:.2f}')
    # Interpretation of bmi
    if(bmi < 16):
        st.error("Severe deficiency body weight")
    elif(bmi > 16 and bmi < 18.5):
        st.warning("Insufficient(deficiency) body weight")
    elif(18.5 < bmi < 25):
        st.success("Standard")
    elif(25 < bmi < 30):
        st.warning("Excess body mass")
    elif(bmi > 30):
        st.error("Sugarholic")