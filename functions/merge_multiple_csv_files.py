import pandas as pd
import os

def merge_multiple_csv_files(folder_path, output_folder= "output"):
    os.makedirs(output_folder, exist_ok=True)

    all_csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                     if file.endswith('.csv')]
    combined_file = pd.concat([pd.read_csv(file) for file in all_csv_files], ignore_index=True)
    output_file = os.path.join(output_folder, "merged_csv.csv")
    combined_file.to_csv(output_file, index=False) 

    return output_file  