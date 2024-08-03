import pandas as pd
import sys
import json

# Load the Parquet file into a DataFrame
parquet_file_path = 'src/data/ano-2023.parquet'
df = pd.read_parquet(parquet_file_path)

# Ensure that 'fact_anual' is properly converted to a float after replacing commas
df['fact_anual'] = df['fact_anual'].str.replace(',', '.').astype(float)

# Perform the calculations
O = df[df['cae_especifico'].between(1, 7)]['fact_anual'].sum()
DO = df[df['cae_especifico'].between(8, 9)]['fact_anual'].sum()
FT = df[df['cae_especifico'].between(1, 9)]['fact_anual'].sum()
MENORES = df[df['edad'] < 15]['fact_anual'].sum()
PET = df[df['edad'] >= 15]['fact_anual'].sum()
TOTAL = df['fact_anual'].sum()

# Create a dictionary to hold the results
results = {
    'O': O,
    'DO': DO,
    'FT': FT,
    'MENORES': MENORES,
    'PET': PET,
    'TOTAL':TOTAL
}

# Convert the results dictionary to a JSON string
results_json = json.dumps(results, ensure_ascii=False, indent=4)

# Print the JSON string to sys.stdout
print(results_json, file=sys.stdout)