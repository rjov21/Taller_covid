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

data.loc[data['Estado'] == 'leve', 'Estado'] = 'Leve'
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
data.loc[data['Sexo'] == 'Fallecido'] = 'F'



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



#11 Liste de mayor a menor los 10 departamentos con mas casos de contagiados
departamentos_afectados = data['Nombre departamento'].value_counts().head(10)


# 12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
aux12 = data.loc[(data['Estado'] == 'Fallecido')]
departamentos_mas_fallecidos = aux12['Nombre departamento'].value_counts().head(10)


# 13 Liste de mayor a menor los 10 departamentos con mas casos de recuperados
aux13 = data.loc[(data['Recuperado'] == 'Recuperado')]
departamentos_mas_recuperados = aux13['Nombre departamento'].value_counts().head(10)


# 14  Liste de mayor a menor los 10 municipios con mas casos de contagiados
municipios_afectados = data['Nombre municipio'].value_counts().head(10)



# 15 Liste de mayor a menor los 10 municipios con mas casos de fallecidos
aux15 = data.loc[(data['Estado'] == 'Fallecido')]
municipios_mas_fallecidos = aux15['Nombre municipio'].value_counts().head(10)


# 16 . Liste de mayor a menor los 10 municipios con mas casos de recuperados
aux16 = data.loc[(data['Recuperado'] == 'Recuperado')]
departamentos_mas_recuperados = aux16['Nombre municipio'].value_counts().head(10)


# 17 Liste agrupado por departamento y en orden de Mayor a menor las ciudades 
#con mas casos de contagiados
agrupado_departamentos_mas_contagiados = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values( ascending=False)


# 18  Número de Mujeres y hombres contagiados por ciudad por departamento
cantidad_mujeres_hombres = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()


# 19 Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
edad_promedio = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo',])['Edad'].describe()


# 20 Liste de mayor a menor el número de contagiados por país de procedencia




# 21 . Liste de mayor a menor las fechas donde se presentaron mas contagios
listado_fechas = data['fecha reporte web'].value_counts().sort_values( ascending=False)


#22 Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
numero_muertes = data.loc[(data['Estado'] == 'Fallecido')].shape[0]
cantidad_casos = data.shape[0]
tasa_mortalidad = numero_muertes / cantidad_casos * 100


numero_recuperados = data.loc[(data['Recuperado'] == 'Recuperado')].shape[0]
cantidad_casos_recuperados = data.shape[0]
tasa_recuperados = numero_recuperados / cantidad_casos_recuperados * 100


# 23 Liste la tasa de mortalidad y recuperación que tiene cada departamento
numero_muertes = data.loc[(data['Estado'] == 'Fallecido')].shape[0]
cantidad_casos = data['Nombre departamento']
tasa_mortalidad = numero_muertes / cantidad_casos * 100
tasa_mortalidad_departamentos = [tasa_mortalidad]
data['Tasa mortalidad departamentos'] = tasa_mortalidad_departamentos
