from functions.restructure_csv_layout import restructure_csv_layout as restructure
import pandas as pd
import os

def test_restructure_csv_layout():
    csv_file = "input/test1.csv"
    output_folder = "output"
    result_file = restructure(csv_file, output_folder)
    assert os.path.exists(result_file)
    restructured_df = pd.read_csv(result_file)
    assert len(restructured_df) > 0


