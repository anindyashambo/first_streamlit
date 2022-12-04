import streamlit 
import requests
import pandas 
#import snowflake.connector
streamlit.title("My parents new healthy diner")

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)  
#fruits_selected = streamlit.multiselect("pick me some fruits :",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)  


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())



fruit_choice = streamlit.text_input('What fruit would you like information about?','Lime')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)
streamlit.write("thanks for adding",add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')")
#streamlit.text(my_data_row)

