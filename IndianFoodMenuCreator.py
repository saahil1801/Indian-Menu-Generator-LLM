import streamlit as st
import langchaincode

st.title("Restaurant Name Generator")

indianfood = st.sidebar.selectbox("Pick a Food", ("Samosa", "NorthIndianFood", "Panipuri Chaats", "Indian Kulfi", "Chicken Tandoori", "Dosa",'Pav Bhaji'))

if indianfood:
    response = langchaincode.generate_restaurant_name_and_items(indianfood)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)
        st.markdown("  ")