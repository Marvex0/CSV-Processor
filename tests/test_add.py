from functions.append_csv_files import append_csv_files as append

csv_file1 = "input/test1.csv"
csv_file2 = "input/test2.csv"
output_folder = "output"
result_file = append(csv_file1, csv_file2, output_folder)
print(f"Appended file created: {result_file}")