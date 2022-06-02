# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:38:01 2022

@author: ABC
"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID_19_en_Colombia.csv'
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
data.loc[data['Estado'] == 'LEVE', 'Estado'] = 'Leve'

# Cuantas personas murieron por covid en Colombia
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm', 'Sexo'] = 'M'
data.loc[data['Sexo'] == 'f', 'Sexo'] = 'F'

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

data.loc[data['Estado'] == 'M', 'Estado'] = 'Moderado'
data.loc[data['Sexo'] == 'Fallecido', 'Estado'] = 'F'



#1 Número de casos de Contagiados en el País
data['fecha reporte web'].count()


#2 Número de Municipios Afectados
data['Nombre municipio'].value_counts().shape


#3 Liste los municipios afectados (sin repetirlos)
# normalizar nombre municipio
data.loc[data['Nombre municipio'] == 'BOGOTA', 'Nombre municipio'] = 'Bogota'
data.loc[data['Nombre municipio'] == 'Fallecido', 'Nombre municipio'] = 'Fallecido'
data.loc[data['Nombre municipio'] == 'puerto COLOMBIA', 'Nombre municipio'] = 'puerto colombia'
#3 Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].unique()



# Normalizar Ubicación del caso
data.loc[data['Ubicación del caso'] == 'CASA', 'Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'casa', 'Ubicación del caso'] = 'Casa'
#4 Número de personas que se encuentran en atención en casa
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
Cantidad_casa = aux.shape[0]



# normalizar Recuperado
data.loc[data['Recuperado'] == 'fallecido', 'Recuperado'] = 'Fallecido'
# 5 Número de personas que se encuentran recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado') ]
cantidad_recuperados = aux.shape[0]


#6 Número de personas que ha fallecido
cantidad_fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]


#7 Ordenar de Mayor a menor por tipo de caso
data['Tipo de contagio'].value_counts().head(10)


# normalizar nombre departamento
data.loc[data['Nombre departamento'] == 'Tolima', 'Nombre departamento'] = 'TOLIMA'
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
data['Nombre del país'].value_counts()



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
aux_numero_muertes = data.loc[(data['Estado'] == 'Fallecido')]
for x in range(aux_numero_muertes['Nombre departamento'].value_counts().shape[0]):
    print(aux_numero_muertes['Nombre departamneot'].value_counts().index[x])
    tasa_mortalidad = (aux_numero_muertes['Nombre departamento'].value_counts().iloc[x] / data['Nombre municipio'].value_counts().iloc[x]) * 100
    print(tasa_mortalidad)



# 24 Liste la tasa de mortalidad y recuperación que tiene cada ciudad
aux_numero_muertes = data.loc[(data['Estado'] == 'Fallecido')]
for x in range(aux_numero_muertes['Nombre municipio'].value_counts().shape[0]):
    print(aux_numero_muertes['Nombre municipio'].value_counts().index[x])
    tasa_mortalidad = (aux_numero_muertes['Nombre municipio'].value_counts().iloc[x] / data['Nombre municipio'].value_counts().iloc[x]) * 100
    print(tasa_mortalidad)


# normalizar Tipo de recuperación
data.loc[data['Tipo de recuperación'] == 'F', 'Tipo de recuperación'] = 'Fallecido'
# 25  Liste por cada ciudad la cantidad de personas por atención
data.groupby([ 'Nombre municipio', 'Tipo de recuperación']).size()


data.loc[data['Edad'] == 'NaN', 'Edad'] = 0
# 26 Liste el promedio de edad por sexo por cada ciudad de contagiados
data.groupby([ 'Nombre municipio', 'Edad']).describe()


# 27 Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados

data[(data['Estado'] == 'Fallecido') ].groupby('Fecha de diagnóstico').size().plot()



# 30 Liste de mayor a menor la cantidad de fallecidos por edad en todaColombia.
data.groupby(['Edad', 'fecha reporte web']).size().value_counts().head(40)


# 31 Liste el porcentaje de personas por atención de toda Colombia
data['Tipo de recuperación'].value_counts().mean()


# 32 Haga un gráfico de barras por atención de toda Colombia
data['Tipo de recuperación'].value_counts().plot(kind = 'bar')


# 33 Haga un gráfico de barras por Sexo de toda Colombia
data['Sexo'].value_counts().plot(kind = 'bar')


# 34 Haga un gráfico de barras por tipo de toda Colombia
data['Tipo de contagio'].value_counts().plot(kind = 'bar')


# 35 Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia
data.groupby(['Estado', 'fecha reporte web', 'Recuperado']).plot(kind = 'bar')

