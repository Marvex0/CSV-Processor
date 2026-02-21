from functions.split_csv_by_column import split_csv_by_column as split_column

csv_file = "input/test1.csv"
output_folder = "output"
result_files = split_column(csv_file, output_folder)
print("Generated files:")
for file in result_files:
    print(file)