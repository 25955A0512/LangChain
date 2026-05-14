import streamlit as st
import Langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", 
                               ("Indian", "Italian", "Chinese", "Arabic", "American"))

if cuisine:
    response = Langchain_helper.generate_restaurent_name_and_items(cuisine)
    res_name = response['restaurent_name'].content
    menu_text = response['menu'].content 
    st.header(res_name.strip('"')) # strip quotes if the AI adds them
    menu_items = menu_text.split(",")
    
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("->", item.strip())