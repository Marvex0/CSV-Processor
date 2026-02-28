from functions.merge_multiple_csv_files import merge_multiple_csv_files as merge
import pandas as pd
import os

def test_merge_multiple_csv_files():
    folder_path = "input"
    output_folder = "output"
    result_file = merge(folder_path, output_folder)
    assert os.path.exists(result_file)
    combined_df = pd.read_csv(result_file)
    assert len(combined_df) > 0
