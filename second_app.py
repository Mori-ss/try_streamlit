
import re
import streamlit as st
import pandas as pd
import numpy as np


### reading dataset(csv file) from local directory

# path to cars datasets
url = "C:/Users/ssunk/PycharmProjects/PracticeForDS/studystreamlit/Cars Datasets 2025.csv"

# for loading dates
@st.cache_data
def load_data():
    return pd.read_csv(url, encoding = 'cp1252')

### Cleaning dataset

# Function to clean and extract numeric average from CC/Battery Capacity
def clean_capacity(cell):
    if not isinstance(cell, str):
        return np.nan
    numbers = re.findall(r'\d+(?:\.\d+)?', cell.replace(",", ""))
    numbers = [float(num) for num in numbers]
    return sum(numbers) / len(numbers) if numbers else np.nan

def clean_numeric_cell(cell):
    if pd.isnull(cell):
        return np.nan
    cell = str(cell).replace(",", "")
    numbers = re.findall(r'\d+(?:\.\d+)?', cell)
    numbers = [float(num) for num in numbers]
    return sum(numbers) / len(numbers) if numbers else np.nan

# load data
cars_df = load_data()

# Apply the function to create a new cleaned column
cars_df['Cleaned Capacity'] = cars_df['CC/Battery Capacity'].apply(clean_capacity)

# List of columns to clean
columns_to_clean = [
    'HorsePower',
    'Total Speed',
    'Performance(0 - 100 )KM/H',
    'Cars Prices',
    'Seats',
    'Torque'
]

# Apply the function to each column
for col in columns_to_clean:
    cars_df[col] = cars_df[col].apply(clean_numeric_cell)

# Save cleaned file (optional)
# cars_df.to_csv("Cars_Dataset_Cleaned.csv", index=False)


### Function get dataframe that with selected category after clicking apply
def get_filtered_cars(show_data, car_name, use_price, selected_company,selected_fuel_types):
    result_df = cars_df.copy()

    # show whole dataframe without any filters
    if show_data:
        st.subheader("Raw data")
        st.dataframe(cars_df)

    # filter by car name
    if car_name:
        # st.subheader(f"Cars by name {car_name}")
        if car_name in cars_df['Cars Names'].values:
            result_df = result_df[result_df['Cars Names'] == car_name]

    # filter by price range if selected
    if use_price:
        # st.subheader(f"Cars between price {slider_range[0]} and {slider_range[1]}")
        result_df = result_df[
            (result_df['Cars Prices'] >= slider_range[0]) &
            (result_df['Cars Prices'] <= slider_range[1])
        ]


    if selected_fuel_types:
        result_df = result_df[result_df['Fuel Types'].isin(selected_fuel_types)]
    if selected_company:
        # st.subheader('Cars by companies name:')
        # st.text(", ".join(selected_company))
        result_df = result_df[result_df['Company Names'].isin(selected_company)]


    return result_df.sort_values('Company Names')

st.title("Auto Data Dashboard")

st.sidebar.header("Filters")

with st.sidebar.form("Filters"):
    st.info("""Use these option to filter the data""")

    search_car_name = st.text_input("Search by cars name")

    show_raw_data = st.checkbox('Show raw data')

    use_price_range = st.checkbox('Use range price')



    # slider widget for selecting car price range
    price_l = list(cars_df['Cars Prices'].values)
    slider_range = st.slider("Choose the range prices of car", min_value=int(min(price_l)), max_value=int(max(price_l)), value=[5000, 700000])

    cars_company_options = list(set(cars_df['Company Names'].values))
    selected_company = st.multiselect('Sort by Company names',options=cars_company_options)

    fuel_types_options = list(set(cars_df['Fuel Types'].values))
    selected_fuel_types = st.multiselect('Choose types of fuels', options=fuel_types_options)

    submitted = st.form_submit_button('Apply Filters')


if submitted:
    # for check the result of filters
    after_filters = get_filtered_cars(show_raw_data, search_car_name, use_price_range, selected_company, selected_fuel_types)

    if not after_filters.empty:
        st.dataframe(after_filters)
    else:
        st.warning("No cars match the selected filters")