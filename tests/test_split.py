from functions.split_csv_by_row_count import split_csv_by_row_count as split
import pandas as pd
import os

def test_split_csv_by_row_count():
    csv_file = "input/test1.csv"
    row_limit = 2
    output_folder = "output"

    result_files = split(csv_file, row_limit, output_folder)

    assert len(result_files) > 0

    for file in result_files:
        assert os.path.exists(file)
        split_part = pd.read_csv(file)
        assert len(split_part) <= row_limit
