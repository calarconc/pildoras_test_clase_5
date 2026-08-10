import streamlit as st

st.title("Conversor de temperatura")
celsius = st.number_input("Grados Celsius")
fahrenheint =celsius * 9/5+32
st.write(f"{celsius} °c son {fahrenheint} °f")
