import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
import webbrowser

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = 'gemini-pro'

st.set_page_config(
    page_title="Home",
)


st.header("HOSTELAVIE VARANASI")
st.subheader("About Us")
st.write('Featuring views of the Ganges River, this down-to-earth hostel is 3 km from the Shiva Shri Kashi Vishwanath Temple and 5 km from the 18th-century Ramnagar Fort. Lal Bahadur Shastri International Airport is 27 km away.')
st.write('No-nonsense private rooms and mixed-gender or female-only dorms feature en suite or shared bathrooms. Some have air conditioning, and/or bunk beds with reading lights.')
st.write('Amenities consist of lounges, 2 dining areas and a kitchen, plus a terrace and a rooftop cafe. There are guest laundry facilities. Wi-Fi, breakfast and parking are available.')


def open_website():
    url = "https://www.hostelavie.com/booking-engine" 
    webbrowser.open_new_tab(url)

if st.button('Book Now'):
    open_website()


