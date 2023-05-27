import requests
import pandas as pd
API_KEY = 'GiPC6nElewHV97iKyDWlA5tuPljHZCpcgeaT7woa'
#Obtencion de API
url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}'
response = requests.get(url)
data = response.json()

#Creacion de Data frame con las columnas seleccionadas
asteroids = data['near_earth_objects']
df = pd.DataFrame(asteroids,columns=['id', 'neo_reference_id', 'name', 'absolute_magnitude_h', 'estimated_diameter', 'is_potentially_hazardous_asteroid','close_approach_data'])

#Funcion para separar columnas con subvariables 
def separate_estimated_diameter(row):
    diameter = row['estimated_diameter']
    km = diameter['kilometers']
    meters = diameter['meters']
    return pd.Series([km['estimated_diameter_min'], km['estimated_diameter_max'], meters['estimated_diameter_min'], meters['estimated_diameter_max']])

# Aplicar la función a la columna 'estimated_diameter' para separarla en columnas individuales
df[['Dkm_min', 'Dkm_max', 'Dmeters_min', 'Dmeters_max']] = df.apply(separate_estimated_diameter, axis=1)

#Estandarizacion de las variables
df['Dkm_min'] = df['Dkm_min'].round(2)
df['Dkm_max'] = df['Dkm_max'].round(2)
df['Dmeters_min'] = df['Dmeters_min'].round(2)
df['Dmeters_max'] = df['Dmeters_max'].round(2)

# Eliminar la columna 'estimated_diameter' original
df = df.drop('estimated_diameter', axis=1)

##Crear segunda tabla 
# Crear una nueva tabla para separar la columna 'close_approach_data'
df_close_approach = pd.DataFrame(columns=['neo_reference_id', 'Relative_velocity_km/h', 'miss_distance_km', 'miss_distance_lunar', 'orbiting_body', 'approach_date'])

# Iterar sobre cada fila del dataframe original
for index, row in df.iterrows():
    approach_data = row['close_approach_data']
    if approach_data:
        for approach in approach_data:
            approach_dict = {
                'neo_reference_id': row['neo_reference_id'],
                'Relative_velocity_km/h': approach['relative_velocity']['kilometers_per_hour'],
                'miss_distance_km': approach['miss_distance']['kilometers'],
                'miss_distance_lunar': approach['miss_distance']['lunar'],
                'orbiting_body': approach['orbiting_body'],
                'approach_date': approach['close_approach_date']
            }
            df_close_approach.loc[len(df_close_approach)] = approach_dict

# Convertir columnas a tipo numérico
df_close_approach['Relative_velocity_km/h'] = pd.to_numeric(df_close_approach['Relative_velocity_km/h'], errors='coerce')
df_close_approach['miss_distance_km'] = pd.to_numeric(df_close_approach['miss_distance_km'], errors='coerce')
df_close_approach['miss_distance_lunar'] = pd.to_numeric(df_close_approach['miss_distance_lunar'], errors='coerce')

# Redondear las variables a 2 decimales
df_close_approach['Relative_velocity_km/h'] = df_close_approach['Relative_velocity_km/h'].round(2)
df_close_approach['miss_distance_km'] = df_close_approach['miss_distance_km'].round(2)
df_close_approach['miss_distance_lunar'] = df_close_approach['miss_distance_lunar'].round(2)

# Visualizar la tabla
print(df_close_approach.to_string(index=False))
