import streamlit as st
import pandas as pd


st.title('Rentabilidad de objetos de cria')

st.subheader('DATOS')
DATA=pd.read_csv('DATA.csv', sep=';')
DATA['Rendimiento']=DATA['Eficacia']*DATA['Usos']
DATA['R/P']=DATA['Rendimiento']/DATA['Precio']


DATA1=DATA.query("Item=='Abrevadero'")
DATA1RP=DATA1['R/P']
DATA2=DATA.query("Item=='Aporreadora'")
DATA2RP=DATA2['R/P']
DATA1MEDIAN=DATA1RP.median()
DATA2MEDIAN=DATA2RP.median()
#DATA1ORDENADO=DATA1.sort_values(by='Nivel', ascending=False)

st.write(DATA)
st.subheader('Abrevaderos')
st.write(DATA1)
st.subheader('Aporreadoras :slightly_smiling_face:')
st.write(DATA2)
#st.write(DATA1MEDIAN)
#st.write(DATA2MEDIAN)
