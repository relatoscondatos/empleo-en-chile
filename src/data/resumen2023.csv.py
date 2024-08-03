import pandas as pd
import sys
import json

# Load the Parquet file into a DataFrame
#parquet_file_path = 'src/data/ano-2023.parquet'
#df = pd.read_parquet(parquet_file_path)

# Ensure that 'fact_anual' is properly converted to a float after replacing commas
#df['fact_anual'] = df['fact_anual'].astype(str).str.replace(',', '.').astype(float)

# Perform the calculations
results = {
    'O': 1
}

# Create a DataFrame from the results
results_df = pd.DataFrame([results])

# Write the data frame to CSV, and to standard output
results_df.to_csv(sys.stdout)

# Convert the DataFrame to JSON string
#results_json = results_df.to_json(orient='records', lines=True)

# Print the JSON string to sys.stdout
#print(results_json, file=sys.stdout)
# Convert the results dictionary to a JSON string
#results_json = json.dumps(results, ensure_ascii=False, indent=4)

# Print the JSON string to sys.stdout
#print(results_json, file=sys.stdout)