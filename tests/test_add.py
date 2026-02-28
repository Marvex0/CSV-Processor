from functions.append_csv_files import append_csv_files as append
import pandas as pd
import os

def test_append_csv_files():
    csv_file1 = "input/test1.csv"
    csv_file2 = "input/test2.csv"
    output_folder = "output"
    result_file = append(csv_file1, csv_file2, output_folder)

    assert os.path.exists(result_file)
    combined_df = pd.read_csv(result_file)
    assert len(combined_df) > 0






