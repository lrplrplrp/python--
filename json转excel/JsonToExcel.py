import pandas as pd
import os 
import glob

def change_file_extension(file_path, new_extension):
    file_path_without_extension, current_extension = os.path.splitext(file_path)
    new_file_path = file_path_without_extension + '.' + new_extension
    return new_file_path

for filename in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.txt')):
    df = pd.read_json(filename,dtype=object)
    df=df.astype(str)
    df.to_excel(change_file_extension(filename, 'xlsx'), index=False)
