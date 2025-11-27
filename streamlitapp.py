# dashboard.py
import streamlit as st
import requests

BASE_URL = "https://cloud-flask-server.onrender.com"

st.title("Class IoT / Robotics Dashboard")

group_id = st.number_input("Filter by group ID (0 = all)", min_value=0, step=1, value=0)

if group_id == 0:
    res = requests.get(f"{BASE_URL}/log")
else:
    res = requests.get(f"{BASE_URL}/log/{group_id}")

data = res.json() or []

st.write(f"Total entries: {len(data)}")
st.json(data)
