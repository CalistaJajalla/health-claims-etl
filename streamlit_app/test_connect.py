import streamlit as st
import socket

host = st.secrets["POSTGRES_HOST"]
port = int(st.secrets["POSTGRES_PORT"])

try:
    # Try IPv6
    info6 = socket.getaddrinfo(host, port, socket.AF_INET6)
    st.write("IPv6 addresses:", [i[4][0] for i in info6])
except Exception as e:
    st.write("IPv6 resolution error:", e)

try:
    # Try IPv4
    info4 = socket.getaddrinfo(host, port, socket.AF_INET)
    st.write("IPv4 addresses:", [i[4][0] for i in info4])
except Exception as e:
    st.write("IPv4 resolution error:", e)
