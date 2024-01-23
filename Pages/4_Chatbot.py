import streamlit as st

import streamlit as st

def page4():
    st.title("Page 4")

rooms_data = [
    {
        "room_type": "Familiar 3-4 people",
        "availability": 4,
        "price": 2600,
    },
    {
        "room_type": "Classic Double Bedroom AC",
        "availability": 2,
        "price": 1500,
    },
    {
        "room_type": "7 Bedroom AC",
        "availability": 7,
        "price": 4000,
    }
]

def get_room_details(room_type):
    for room in rooms_data:
        if room_type.lower() in room["room_type"].lower():
            return room
    return None

def display_room_details(room_details):
    st.subheader(room_details["room_type"])
    st.write(f"Availability: {room_details['availability']} rooms")
    st.write(f"Price: ${room_details['price']} per night")

def main():
    st.title("Hotel Booking Chatbot")

    st.header("Ask about a room type:")

    # Use a dropdown menu instead of a text input
    room_types = [room["room_type"] for room in rooms_data]
    user_input = st.selectbox("Select a room type:", room_types)

    if st.button("Submit"):
        if not user_input:
            st.warning("Please select a room type.")
        else:
            room_details = get_room_details(user_input)
            if room_details:
                display_room_details(room_details)
            else:
                st.warning(f"Room type '{user_input}' not found. Please select a valid room type.")

if __name__ == "__main__":
    main()
