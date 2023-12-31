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
# streamlit.dataframe(my_fruit_list)- since we are adding other features like multiselect, let's not display the frame twice. for now we'll comment it out

# We'll add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies. Let's put a pick list here so they can pick the fruit they want to include ; 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) modification below so comment out for now;

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)

# We'll ask our app to put the list of selected fruits into a variable called fruits_selected. Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set 
# (and assign that data to a variable called fruits_to_show). Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())



