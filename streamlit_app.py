import streamlit 
import requests
import pandas as pd 
import snowflake.connector
from urllib.error import URLError


streamlit.title("My parents new healthy diner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)  

    ## repeateable code 
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
   return(fruityvice_normalized)
  
   ## new section to display  
streamlit.header("Fruityvice fruit advice")

try :
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
      streamlit.error("please select to get fruit info")
    else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
        
except URLError as e:
  streamlit.error()        
       
streamlit.header("The fruit load list contains")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_car.execute("select * from fruit_load_list")
    return my_cur.fetchall()
                   
# Add a button to load the fruit
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
    
        
                        
# allow the end user to add a fruit to the list 
                   
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur :
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('guava')")
        return "Thanks for adding " + new_fruit
        
                          
add_my_fruit =  streamlit.text_input('what fruit do you want to add')   
if streamlit.button('Add a fruit to the list'):
                   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
                   back_from_function = insert_row_snowflake(add_my_fruit)
                   streamlit.text(back_from_function)
                
                   
                   


                   
