from functions.split_csv_by_column import split_csv_by_column as split_column
import pandas as pd
import os

def test_split_csv_by_column():
    csv_file = "input/test1.csv"
    output_folder = "output"
    result_files = split_column(csv_file, output_folder)
    assert len(result_files) > 0

    for file in result_files:
        assert os.path.exists(file)
        split_part = pd.read_csv(file)
        assert len(split_part.columns) > 0
