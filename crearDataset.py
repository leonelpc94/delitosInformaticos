import pandas as pd
import json
with open("departamentosInfo.json","r") as json_file:
    data = json.load(json_file)
dataframe = pd.read_csv("Delitos_Informaticos_V1_20240924.csv")
dataframe = dataframe.drop(columns=['CRIMINALIDAD', 'ES_ARCHIVO','ESTADO','ETAPA_CASO','PAÍS_HECHO','SECCIONAL','CONSUMADO','GRUPO_DELITO','LEY'])
filtroHechos = dataframe[(dataframe["AÑO_HECHOS"]>=2020) & (dataframe["AÑO_HECHOS"]<=2023)]
filtroHechos['shape_leng'] =None
filtroHechos['shape_area'] =None
##############################################################################################
for departamento in data:
    filtroHechos.loc[filtroHechos['DEPARTAMENTO_HECHO']==departamento['nombre'],'shape_leng'] = departamento['superficie']['shape_leng']
    filtroHechos.loc[filtroHechos['DEPARTAMENTO_HECHO']==departamento['nombre'],'shape_area'] = departamento['superficie']['shape_area']
    filtroHechos.loc[filtroHechos['DEPARTAMENTO_HECHO']==departamento['nombre'],'dpto_narea'] = departamento['superficie']['dpto_narea']

filtroHechos.to_csv("datasetInfo.csv", index =False)