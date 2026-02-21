import pandas as pd
import os

def restructure_csv_layout(csv_file, output_folder= "output"):
    os.makedirs(output_folder, exist_ok=True)
    read_file = pd.read_csv(csv_file)
    transposed_file = read_file.transpose()
    output_file = os.path.join(output_folder, f"restructured_{os.path.basename(csv_file)}")
    transposed_file.to_csv(output_file, header=False)
    return output_file

