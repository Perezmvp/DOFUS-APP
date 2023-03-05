import streamlit as st
import pandas as pd


st.title('Rentabilidad de objetos de cria')
NOMBRE_OPCIONES=['Todos','Acariciadoras','Aporreadoras','Dragonalgas','Abrevaderos','Fulminadoras']
OPCIONES=st.radio('Filtrar por:',NOMBRE_OPCIONES)

DATAINDEX=pd.read_csv('DATA.csv', sep=';')
DATA=DATAINDEX.style.hide_index()
DATA['Rendimiento']=DATA['Eficacia']*DATA['Usos']
DATA['R/P']=DATA['Rendimiento']/DATA['Precio']

ACARICIADORAS=DATA.query("Item=='Acariciador'")
APORREADORAS=DATA.query("Item=='Aporreadora'")
DRAGONALGAS=DATA.query("Item=='Dragonalgas'")
ABREVADEROS=DATA.query("Item=='Abrevadero'")
FULMINADORAS=DATA.query("Item=='Fulminadora'")

ACARICIADORASRP=ACARICIADORAS['R/P']
APORREADORASRP=APORREADORAS['R/P']
DRAGONALGASRP=DRAGONALGAS['R/P']
ABREVADEROSRP=ABREVADEROS['R/P']
FULMINADORASRP=FULMINADORAS['R/P']

ACARICIADORASMEDIAN=ACARICIADORASRP.median()
APORREADORASMEDIAN=APORREADORASRP.median()
DRAGONALGASMEDIAN=DRAGONALGASRP.median()
ABREVADEROSMEDIAN=ABREVADEROSRP.median()
FULMINADORASMEDIAN=FULMINADORASRP.median()

ACARICIADORAS['Rentabilidad']=ACARICIADORAS['R/P']/ACARICIADORASMEDIAN
APORREADORAS['Rentabilidad']=APORREADORAS['R/P']/APORREADORASMEDIAN
DRAGONALGAS['Rentabilidad']=DRAGONALGAS['R/P']/DRAGONALGASMEDIAN
ABREVADEROS['Rentabilidad']=ABREVADEROS['R/P']/ABREVADEROSMEDIAN
FULMINADORAS['Rentabilidad']=FULMINADORAS['R/P']/FULMINADORASMEDIAN

TODOS=pd.concat([ACARICIADORAS,APORREADORAS,DRAGONALGAS,ABREVADEROS,FULMINADORAS], ignore_index=True)

if OPCIONES == 'Todos':
    st.subheader('TODOS :earth_americas:')
    st.write(TODOS)
if OPCIONES == 'Acariciadoras':
    st.subheader('ACARICIADORAS :smile:')
    st.write(ACARICIADORAS)
if OPCIONES == 'Aporreadoras':
    st.subheader('APORREDORAS :rage:')
    st.write(APORREADORAS)
if OPCIONES == 'Dragonalgas':
    st.subheader('DRAGONALGAS :peach:')
    st.write(DRAGONALGAS)
if OPCIONES == 'Abrevaderos':
    st.subheader('ABREVADEROS :droplet:')
    st.write(ABREVADEROS)
if OPCIONES == 'Fulminadoras':
    st.subheader('FULMINADORAS :zap:')
    st.write(FULMINADORAS)

#st.subheader('Abrevaderos')
#st.write(ABREVADEROS)
#st.subheader('Aporreadoras :slightly_smiling_face:')
#st.write(APORREADORAS)
#st.write(ABREVADEROSMEDIAN)
#st.write(APORREADORASMEDIAN)
