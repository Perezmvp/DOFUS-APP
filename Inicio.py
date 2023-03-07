import streamlit as st
import gspread

gc = gspread.service_account(filename='DOFUS TOOLS API KEY.json')
Manitas = gc.open('DATA').worksheet('CRIA')
Manitas.update_cell(20,1, 'SEBASTIAN')