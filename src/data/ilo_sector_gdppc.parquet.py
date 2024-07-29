import pandas as pd
import io
import sys

# Load the first parquet file
emp_file_path = "src/data/EMP_TEMP_SEX_INS_NB_A-20240725T0039.parquet"
emp_df = pd.read_parquet(emp_file_path)

# Filter the first DataFrame
filtered_emp_df = emp_df[(emp_df['sex'] == 'Total')]

# Pivot the DataFrame to get 'sector' values as columns
pivoted_emp_df = filtered_emp_df.pivot_table(index=['country', 'countryCode', 'time'], columns='sector', values='value').reset_index()

# Handle division by zero and NaN values
pivoted_emp_df['publicPercentage'] = pivoted_emp_df['Public'] / pivoted_emp_df['Total'].replace(0, pd.NA)

# Sort the DataFrame by 'country' and 'time' in descending order
sorted_emp_df = pivoted_emp_df.sort_values(by=['country', 'time'], ascending=[True, False])

# Get the latest record for each country
latest_emp_records_df = sorted_emp_df.drop_duplicates(subset=['country'], keep='first')

# Load the second parquet file
gdp_file_path = "src/data/gdp_per_capita_ppp_current_international$.parquet"
gdp_df = pd.read_parquet(gdp_file_path)

# Filter the second DataFrame for the year 2023
gdp_2023_df = gdp_df[gdp_df['year'] == 2023][['countryCode', 'region', 'incomeGroup', 'value']].rename(columns={'value': 'gdppc'})

# Merge the DataFrames on the 'countryCode' column
merged_df = latest_emp_records_df.merge(gdp_2023_df, on='countryCode', how='left')

# Create an in-memory buffer
buffer = io.BytesIO()

# Convert the merged DataFrame to a Parquet file in memory
merged_df.to_parquet(buffer, engine='pyarrow')

# Write the buffer content to sys.stdout
sys.stdout.buffer.write(buffer.getvalue())
