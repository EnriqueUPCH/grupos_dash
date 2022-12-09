import streamlit as st
import pandas as pd 
import numpy as np 
import gdown



st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:")
st.title("SUNEDU - Licenciamiento Institucional")
st.header('**Integrantes:**')

col1, col2, col3,col4,col5 = st.columns(5)

col1.metric("UPCH", "Sebastian", "Saldaña")
col2.metric("UPCH", "Valery", "Siccha")
col3.metric("UPCH", "Gyoran", "Moreno")
col4.metric("UPCH", "Enrique", "Orozco")
col5.metric("UPCH", "Jimena", "Peña")

@st.experimental_memo
def download_data():
	#https://drive.google.com/uc?id=YOURFILEID
	url = "https://drive.google.com/uc?id=1XHTCztia4fEDwsUciKVLmFEFcMAnvT6n"
	output = 'data.csv'
	gdown.download(url,output,quiet = False)
download_data()
st.subheader('**Descripcion**')
st.write("Nuestra presente página es para ayudar a estudiantes y/o padres de familia que busca si cierta universidad está licenciada o no por parte de SUNEDU.")
#tabla general de las universidades(dataset)
st.write("*- A continuación se muestra la tabla general de las universidades con sus datos respectivos*")
st.subheader("Tabla General")
data= pd.read_csv("data.csv",sep="|",  encoding= "latin_1")
data=data.set_index("CODIGO_ENTIDAD")
x= data.set_index("NOMBRE")
st.dataframe(data)
st.info("Informacion de la tabla: https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional")

set_universidades= data['NOMBRE'].dropna().unique()


#seleccionador por tipo de gestion, ademas muestra una tabla por orden de gestion
st.write("""
	*- Seleccione “Privado” o “Público” para que así le muestre las universidades por su tipo de gestión, además de la información del estado de licenciamiento de la universidad*
	""")

esta= data["TIPO_GESTION"].unique()
licensi= data["ESTADO_LICENCIAMIENTO"].unique()
estado=st.selectbox("Gestion tipo:",("Publico","Privado"))


if estado== "Publico":
    public= data.loc[data.loc[:,"TIPO_GESTION"]=="PÚBLICO"]
    st.dataframe(data.loc[data.loc[:,"TIPO_GESTION"]=="PÚBLICO"])
elif estado== "Privado":
    public= data.loc[data.loc[:,"TIPO_GESTION"]=="PRIVADO"]
    st.dataframe(data.loc[data.loc[:,"TIPO_GESTION"]=="PRIVADO"])

#seleccionador para comparar el periodo de licenciamiento de diferentes universidades, así mismo muestra la información de la universidad seleccionada
st.write("""
	*- A continuación usted podrá comparar diferentes universidades por su “Periodo de licenciamiento”, además le mostrará solo la información de las universidades seleccionadas*
	""")
opti= st.multiselect(
    "Seleccione las universidades que desea comparar la el periodo de licenciamiento", 
    options= data["NOMBRE"].unique()
    )
para= x.loc[opti]
st.dataframe(para)
baraa= x.loc[opti,"PERIODO_LICENCIAMIENTO"]

st.bar_chart(baraa)
