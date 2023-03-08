import streamlit as st
import pandas as pd
import gspread

st.title('Rentabilidad de objetos de cria')

tab1, tab2= st.tabs(["All-might-man", "Alejandraz"])

with tab1:
    gc = gspread.service_account(filename='DOFUS TOOLS API KEY.json')
    INV_PEREZ = gc.open('DATA').worksheet('INV_PÉREZ')
    DATAINVPEREZ = pd.DataFrame(INV_PEREZ.get_all_records())
    
    edited_DATAINVPEREZ = st.experimental_data_editor(DATAINVPEREZ, num_rows='dynamic')
    INV_PEREZ.clear()
    INV_PEREZ.update([edited_DATAINVPEREZ.columns.values.tolist()] + edited_DATAINVPEREZ.tolist())






