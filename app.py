import streamlit as st

st.title("Conversor de temperatura")
modo = st.radio("Convertir de:"["Celsius a Fahrenheit","Farenheit a Celsius"])
valor = st.number_input("valor")
if modo =="Celsius a Fahrenheit":
    resultado = valor *9/5+32
    st.write(f"{valor}°C son {round(resultado, 2)} °F")
elif modo == "Farenheit a Celsius":
    resultado = (valor - 32) * 5/9 
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st

celsius = st.number_input("Grados Celsius")
fahrenheint =celsius * 9/5+32
st.write(f"{celsius} °c son {fahrenheint} °f")
print("Cambios")
