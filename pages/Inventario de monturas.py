import streamlit as st
import pandas as pd
import gspread
tab1, tab2= st.tabs(["All-might-man", "Jalettyz"])
st.title('Rentabilidad de objetos de cria')

with tab1:
    gc = gspread.service_account(filename='DOFUS TOOLS API KEY.json')
    INV_PEREZ = gc.open('DATA').worksheet('INV_PÉREZ')
    DATAINVPEREZ = pd.DataFrame(INV_PEREZ.get_all_records())
    st.write(DATAINVPEREZ)




