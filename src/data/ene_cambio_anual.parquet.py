import pandas as pd
import io
import sys

# Load the parquet file
file_path = "src/data/ene_sintetica.parquet"
data = pd.read_parquet(file_path)
data2 = pd.read_parquet(file_path)

# Load the additional lookup tables from TSV files
actividadEconomica = pd.read_csv("src/data/codigos_actividadEconomica.tsv", sep='\t')
categoriaOcupacion = pd.read_csv("src/data/codigos_categoriaOcupacion.tsv", sep='\t')
grupoOcupacional = pd.read_csv("src/data/codigos_grupoOcupacional.tsv", sep='\t')
formalidadOcupacion = pd.read_csv("src/data/codigos_formalidadOcupacion.tsv", sep='\t')
formalidadSector = pd.read_csv("src/data/codigos_formalidadSector.tsv", sep='\t')
sexo = pd.read_csv("src/data/codigos_sexo.tsv", sep='\t')

# Ensure matching column types before merging
data['b14_rev4cl_caenes'] = data['b14_rev4cl_caenes'].astype(str)
actividadEconomica['code'] = actividadEconomica['code'].astype(str)
data['sexo'] = data['sexo'].astype(str)
sexo['code'] = sexo['code'].astype(str)

data = data.merge(actividadEconomica, left_on='b14_rev4cl_caenes', right_on='code', how='left', suffixes=('', '_actividad'))
data.rename(columns={'desc': 'actividad'}, inplace=True)
print("Columns after merging actividadEconomica:", data.columns,file=sys.stderr)

data = data.merge(categoriaOcupacion, left_on='categoria_ocupacion', right_on='code', how='left', suffixes=('', '_categoria'))
data.rename(columns={'desc': 'categoria'}, inplace=True)

data = data.merge(grupoOcupacional, left_on='b1', right_on='code', how='left', suffixes=('', '_grupo'))
data.rename(columns={'desc': 'grupo'}, inplace=True)

data = data.merge(formalidadOcupacion, left_on='ocup_form', right_on='code', how='left', suffixes=('', '_formalidad_ocupacion'))
data.rename(columns={'desc': 'formalidadOcupacion'}, inplace=True)

data = data.merge(formalidadSector, left_on='sector', right_on='code', how='left', suffixes=('', '_formalidad_sector'))
data.rename(columns={'desc': 'formalidadSector'}, inplace=True)

# Check unique values to ensure they match
print("Unique sexo in data:", data['sexo'].unique(),file=sys.stderr)
print("Unique codes in sexo:", sexo['code'].unique(),file=sys.stderr)

data = data.merge(sexo, left_on='sexo', right_on='code', how='left', suffixes=('', '_sexo'))
data.rename(columns={'desc': 'sexo_desc'}, inplace=True)
# 
# Rename columns as needed
data.rename(columns={
    'ano_trimestre': 'año',
    'mes_central': 'mes'
}, inplace=True)

# Perform the aggregations
result = data.groupby(['año', 'mes']).agg(
    asalariados_sector_publico=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'categoria'] == 'Asalariado sector público'].sum()),
    O=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'Ocupacion'] == 'Ocupados'].sum()),
    DO=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'Ocupacion'] == 'Desocupados'].sum()),
    FT=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[(data.loc[x.index, 'Ocupacion'] == 'Desocupados') | (data.loc[x.index, 'Ocupacion'] == 'Ocupados')].sum()),
    PET=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'edad_de_trabajar'] == 1].sum()),
    sector_informal=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'sector'] == 2].sum()),
    ocupacion_informal=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'ocup_form'] == 2].sum()),
    administracion_publica=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[data.loc[x.index, 'actividad'] == 'O Administración pública y defensa; planes de seguridad social de afiliación obligatoria'].sum()),
    extranjeros=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[(data.loc[x.index, 'Nacionalidad'] == 'Extranjeros') & (data.loc[x.index, 'Ocupacion'] == 'Ocupados')].sum()),
    hombres=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[(data.loc[x.index, 'sexo_desc'] == 'Hombre') & (data.loc[x.index, 'Ocupacion'] == 'Ocupados')].sum()),
    mujeres=pd.NamedAgg(column='fact_cal', aggfunc=lambda x: x[(data.loc[x.index, 'sexo_desc'] == 'Mujer') & (data.loc[x.index, 'Ocupacion'] == 'Ocupados')].sum()),
    personas=pd.NamedAgg(column='fact_cal', aggfunc='sum')
).reset_index()


# Ensure the data is sorted by year and month
result = result.sort_values(by=['mes', 'año'])

# Calculate the year-over-year difference for each field
fields_to_diff = [
    'asalariados_sector_publico', 'O', 'DO', 'FT', 'PET', 
    'sector_informal', 'ocupacion_informal', 'administracion_publica',
    'extranjeros', 'hombres', 'mujeres', 'personas'
]

for field in fields_to_diff:
    result[f'{field}_diff'] = result.groupby('mes')[field].diff()


# Create an in-memory buffer
buffer = io.BytesIO()

# Convert the DataFrame to a Parquet file in memory
result.to_parquet(buffer, engine='pyarrow')

# Write the buffer content to sys.stdout
sys.stdout.buffer.write(buffer.getvalue())

