import streamlit

streamlit.title('My Parents\' New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# '#' is used for commenting

# Let's start using another Python package library. This one is called pandas, and it's very well known among Python developers.  Streamlit includes pandas as part of their core application so we don't need to do anything special except type:
import pandas

# We want pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv  to pull the data into a dataframe we'll call my_fruit_list.
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# then tell streamlit to index the fruit column when allowing multiselect below
my_fruit_list=my_fruit_list.set_index('Fruit')

# After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:
streamlit.dataframe(my_fruit_list)

# We'll add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies. Let's put a pick list here so they can pick the fruit they want to include ; 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let's put a pick list so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
