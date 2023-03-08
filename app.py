import streamlit as st
from aceptador import lexer

st.title('Proyecto 2')
st.markdown('Sea un lenguaje como en L1 = 1(0|1)+11 y sea un segundo lenguaje como en L2 = 11(1|0)∗1. Hagamos un aceptador de cadenas para el lenguaje L3 = L1|L2. El aceptador de cadenas debe pedir la cadena al usuario y responder si lo acepta o no lo hace.')

st.header('Lexer')
cadena = st.text_input('Ingrese la cadena a analizar:')

if st.button('Ingresar'):
    resultado = lexer(cadena)
    st.text(f'Resultado: ${resultado}')

    