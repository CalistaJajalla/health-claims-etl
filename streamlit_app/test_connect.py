import streamlit as st
import socket

host = st.secrets["POSTGRES_HOST"]
port = int(st.secrets["POSTGRES_PORT"])

st.write(f"Testing TCP connection to {host}:{port}...")

try:
    s = socket.create_connection((host, port), timeout=5)
    st.success(f"Connection to {host}:{port} succeeded!")
    s.close()
except Exception as e:
    st.error(f"Connection to {host}:{port} failed: {e}")
