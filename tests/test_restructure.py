from functions.restructure_csv_layout import restructure_csv_layout as restructure

csv_file = "input/test1.csv"
output_folder = "output"    
result_file = restructure(csv_file, output_folder)
print(f"Restructured file created: {result_file}")