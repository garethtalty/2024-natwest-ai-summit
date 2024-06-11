import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

np.random.seed(seed=42)

st.set_page_config(page_title="Streamlit Features Demo 👷")
st.sidebar.header("Streamlit Features Demo 👷")

st.title("Streamlit Features Demo 👷")
st.write("This page demonstrates various Streamlit functionalities that you can use for your app.")

# Text
st.subheader("Text Display")
st.text("This is a simple plain text sentence.")
st.markdown("You can also use markdown to format your text, allowing you to use **bold**, _italics_, `code` etc.")
st.write("`st.write` allows you to use markdown with some additional functionalities, \
    which are detailed here: https://docs.streamlit.io/develop/api-reference/write-magic/st.write.")

# Data Display
st.subheader("Data Display")
data = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write("Here is a sample DataFrame:")
st.dataframe(data)
st.write("You can show a DataFrame as a static table, so it looks a bit nicer:")
st.table(data)

# Interactive Widgets
st.subheader("Interactive Widgets")
st.write("There are a variety of interactive widgets you can use as well.")

st.write("Try out this button:")
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.write("You can also use `text_input` boxes to get information from the user:")
name = st.text_input("Enter your name", "")
st.write(f"Hello, {name}!")

st.write("Sliders can be very handy for gathering information as well:")
age = st.slider("Select your age", min_value=0, max_value=100, value=25)
st.write(f"Your age is {age}")

# Charts
st.subheader("Charts")
st.write("Streamlit is also great at displaying charts:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

# Matplotlib Chart
fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=20)
st.pyplot(fig)

st.write("You can also use Streamlit to display maps:")

# Maps
st.subheader("Maps")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Media
st.subheader("Media")
st.image("https://www.natwest.com/content/dam/natwest_com/Logos/og-logo-nw.png", caption='NatWest Logo')
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3")
st.video("https://www.youtube.com/watch?v=Avqs7nX52mI")

# Layouts
st.subheader("Layouts")
st.write("You can also play around with the layout of the page. Check out this two columns layout:")
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1!")
with col2:
    st.write("This is column 1!")


# File Upload
st.subheader("File Upload")
st.write("You can also upload files to streamlit. Try uploading a csv:")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
