import streamlit as st

instagram_profile_url = "https://www.instagram.com/varanasihostelavie/"

embed_code = f'< src="{instagram_profile_url}" width="500" height="600" frameborder="0" scrolling="no" allowtransparency="true"></iframe>'

try:
    st.markdown(embed_code, unsafe_allow_html=True)
except Exception as e:
    error_message = "Error connecting to Instagram. Please try again later."
    st.markdown(f'<iframe src= width="500" height="600" frameborder="0" scrolling="no" allowtransparency="true"></iframe>', unsafe_allow_html=True)
    st.error(error_message)
