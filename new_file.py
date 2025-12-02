import streamlit as st

st.title("Hello World")
st.subheader("Starting whith Streamlit")
st.text("Choose here interview Round ")
st.write("Good in the First InterView")
a1=st.selectbox("Your Fav Movie :",["Gabber","Thakur","Mogli"])
st.write(f"Your Choose {a1} Excellent Choice")
st.success(f"Your {a1} is too good")