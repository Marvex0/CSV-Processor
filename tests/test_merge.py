from functions.merge_multiple_csv_files import merge_multiple_csv_files as merge

folder_path = "input"
output_folder = "output"
result_file = merge(folder_path, output_folder)
print(f"Merged file created: {result_file}")
