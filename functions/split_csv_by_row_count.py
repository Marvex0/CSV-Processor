import pandas as pd
import os


def split_csv_by_row_count(csv_file, row_count = 100, output_folder= "output"):
    os.makedirs(output_folder, exist_ok=True)
    read_file = pd.read_csv(csv_file)
    total_rows = len(read_file)

    output_files = []
    for i in range(0, total_rows, row_count):
        batch = read_file.iloc[i:i + row_count]
        output_batch = os.path.join(output_folder, f"split_csv_{i // row_count + 1}.csv")
        batch.to_csv(output_batch, index=False)
        output_files.append(output_batch)
    return output_files


    