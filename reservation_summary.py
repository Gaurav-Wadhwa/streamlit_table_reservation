import streamlit as st
import urllib.parse
# Extract query parameters from the URL
query_params = st.query_params
# Extract values correctly and decode them
name = urllib.parse.unquote(query_params.get("name", "UNKNOWN"))
date = query_params.get("date", "Not Provided")
time = query_params.get("time", "Not Provided")
num_people = query_params.get("guests", "0")
st.title("Your Reservation Summary")
st.write(f"### Hello, **{name}**! 🎉")
st.write(f"**Reservation Date:** {date}")
st.write(f"**Reservation Time:** {time}")
st.write(f"**Guests:** {num_people}")
st.success("✅ Your table is reserved successfully! We look forward to hosting you!")

