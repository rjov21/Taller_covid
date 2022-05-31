# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:38:01 2022

@author: ABC
"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimensiones del archivo
data.shape

# Conocer las columnas del arhivo
data.columns

# Cantidad de elementos del arhivo
data.size

# Para saber cuantos registros hay por columna

data.count()

# Acceder a los elementos de una columna
data['Código ISO del país']

# Eliminar columnas de un dataset

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Cuantas personas murieron por covid en Colombia
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Cuantas mujeres fallecieron en Colombia
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') ]
cantidad_muertes_mujeres = aux.shape[0]

# Cuantas personas fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_BQ = aux.shape[0]

# Cuantas mujeres fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_mj_BQ = aux.shape[0]


# Normalizar columna Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'



#1 Número de casos de Contagiados en el País
data['fecha reporte web'].count()


#2 Número de Municipios Afectados
data['Nombre municipio'].value_counts().shape


#3 Liste los municipios afectados (sin repetirlos)
# normalizar nombre municipio
data.loc[data['Nombre municipio'] == 'BOGOTA'] = 'Bogota'
data.loc[data['Nombre municipio'] == 'Fallecido'] = 'Fallecido'
data.loc[data['Nombre municipio'] == 'puerto COLOMBIA'] = 'puerto colombia'
#3 Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].unique()



# Normalizar Ubicación del caso
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
#4 Número de personas que se encuentran en atención en casa
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
Cantidad_casa = aux.shape[0]



# normalizar Recuperado
data.loc[data['Recuperado'] == 'fallecido'] = 'Fallecido'
# 5 Número de personas que se encuentran recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado') ]
cantidad_recuperados = aux.shape[0]


#6 Número de personas que ha fallecido
cantidad_fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]


#7 Ordenar de Mayor a menor por tipo de caso
data['Tipo de contagio'].value_counts().head(10)


# normalizar nombre departamento
data.loc[data['Nombre departamento'] == 'Tolima'] = 'TOLIMA'
#8 Número de departamentos afectados
data['Nombre departamento'].value_counts().shape[0]


#9 Liste los departamentos afectados(sin repetirlos)
data['Nombre departamento'].unique()


#10 Ordene de mayor a menor por tipo de atención 
data['Tipo de recuperación'].value_counts().head(10)

