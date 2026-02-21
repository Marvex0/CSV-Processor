from functions.split_csv_by_row_count import split_csv_by_row_count as split

csv_file = "input/test1.csv"
row_limit = 2
output_folder = "output"

result_files = split(csv_file, row_limit, output_folder)
print("Generated files:")
for file in result_files:
    print(file)