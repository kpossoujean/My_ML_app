import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

######################## plotly ########################"
st.subheader("plotly")
temps=pd.DataFrame({"days":["monday","tuesday","wednesday","thirsday","friday","saturday","sunday"],
                       "temps":[20,28,25,32,10,89,29]})
#st.write(temps)

#histogramme avec plotly
fig=px.bar(
    data_frame=temps,
    x='days',
    y='temps',
    title='Températures moyennes journalières'
)
st.plotly_chart(fig)

#nuage de points avec plotly
data_nuage=pd.DataFrame({"marque":["toyota","toyota","cfao","cfao","rav4","rav4","rav4"],
                         "couleur":["noir","blanc","rouge","rouge","bleue","cendre","cendre"],
                         "pays":["usa","usa","usa","japon","japon","japon","allemagne"],
                         "poids":[20,28,25,32,10,89,29],
                         "cylindre":[10,20,25,40,5,60,11],
                       "temps":[20,28,25,32,10,89,29]})
#st.write(data_nuage)

data_nuage_numeric=data_nuage.select_dtypes(exclude="object").columns.to_list()
var_x=st.selectbox("Choisir la variable d'absisse",data_nuage_numeric)
var_y=st.selectbox("Choisir la variable d'ordonnée",data_nuage_numeric)
data_nuage_categoriel=data_nuage.select_dtypes(include="object").columns.to_list()
var_col=st.selectbox("Choisir la variable pour colorier",data_nuage_categoriel)
fig2=px.scatter(
    data_frame=data_nuage,
    x=var_x,
    y=var_y,
    color=var_col,
    title= str(var_y)+" VS "+str(var_x)
    )

st.plotly_chart(fig2)
