import pandas as pd
import os 
import glob

def change_file_extension(file_path, new_extension):
    file_path_without_extension, current_extension = os.path.splitext(file_path)
    new_file_path = file_path_without_extension + '.' + new_extension
    return new_file_path

for filename in glob.glob(os.path.join(r"./inputFile/", '*.csv')):
    df = pd.read_csv(filename,dtype=object,encoding="GB2312")
    df=df.astype(str)
    df.to_excel(r"./outputFile/"+change_file_extension(os.path.basename(filename), 'xlsx'), index=False)