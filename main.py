import os
from functions.split_csv_by_column import split_csv_by_column as split_column
from functions.split_csv_by_row_count import split_csv_by_row_count as split
from functions.append_csv_files import append_csv_files as append
from functions.merge_multiple_csv_files import merge_multiple_csv_files as merge
from functions.restructure_csv_layout import restructure_csv_layout as restructure

input_folder = "input"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)


merged_file = merge(input_folder, output_folder)
print(f"Merged file created: {merged_file}")

csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
if len(csv_files) >= 2:
    csv_file1 = os.path.join(input_folder, csv_files[0])
    csv_file2 = os.path.join(input_folder, csv_files[1])
    appended_file = append(csv_file1, csv_file2, output_folder)
    print(f"Appended file created: {appended_file}")

split_files_by_row = split(merged_file, row_count=100, output_folder=output_folder)
print("Generated files from row split:")
for file in split_files_by_row:
    print(file) 

split_files_by_column = split_column(merged_file, output_folder)
print("Generated files from column split:")
for file in split_files_by_column:
    print(file) 

restructured_file = restructure(merged_file, output_folder)
print(f"Restructured file created: {restructured_file}")