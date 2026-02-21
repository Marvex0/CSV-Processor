import pandas as pd
import os

def append_csv_files(csv_file1, csv_file2, output_folder= "output"):
    os.makedirs(output_folder, exist_ok=True)
    file1 = pd.read_csv(csv_file1)
    file2 = pd.read_csv(csv_file2)
    combined_file = pd.concat([file1, file2], ignore_index=True)
    output_file = os.path.join(output_folder, "appended_csv.csv")
    combined_file.to_csv(output_file, index=False) 

    return output_file