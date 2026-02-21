import pandas as pd
import os

def split_csv_by_column(csv_file, output_folder= "output"):
    os.makedirs(output_folder, exist_ok=True)
 #   if column_name not in read_file.columns:
 #       raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    
    read_file = pd.read_csv(csv_file)
    output_files = []

    for col_val in read_file.columns:
        col_data = read_file[[col_val]]
        output_file = os.path.join(output_folder, f"{col_val}.csv")
        col_data.to_csv(output_file, index=False)
        output_files.append(output_file)

    return output_files