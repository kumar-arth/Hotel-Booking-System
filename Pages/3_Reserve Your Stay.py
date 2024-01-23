
import streamlit as st
from rooms_data import rooms_data  
from PIL import Image

import streamlit as st

def page3():
    st.title("Page 3")

def main():
    st.title("Hotel Booking System")

    st.header("Room Availability and Prices")

    for room in rooms_data:
        st.subheader(room["room_type"])
        st.write(f"Availability: {room['availability']} rooms")
        st.write(f"Price: ${room['price']} per night")

        
        if st.button(f"Book {room['room_type']}"):
            st.success(f"Room {room['room_type']} booked!")

if __name__ == "__main__":
    main()
