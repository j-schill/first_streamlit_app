import streamlit as sl
import pandas as pd

sl.title('My Parents New Healthy Dinner')

sl.header('Breakfast Menu')

sl.text('Omega 3 & Blueberry Oatmeal')
sl.text('Kale, Spinach & Rocket Smoothie')
sl.text('Hard-Boiled Free-Range Egg')


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
