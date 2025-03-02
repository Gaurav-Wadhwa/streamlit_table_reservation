import streamlit as st
import urllib.parse

# Extract query parmeters from URL
query_params = st.query_params
name = query_params.get("name", ["UNKNOWN"])[0]
date = query_params.get("date", ["Not Provided"])[0]
time = query_params.get("time", ["Not Provided"])[0]
num_people = query_params.get("guests", ["0"])[0]

st.title("Your Reservation Summary")

st.write(f"### Hello, **{name}**! 🎉")
st.write(f"**Reservation Date:** {date}")
st.write(f"**Reservation Time:** {time}")
st.write(f"**Guests:** {num_people}")

st.success("✅ Your table is reserved successfully! We look forward to hosting you!")