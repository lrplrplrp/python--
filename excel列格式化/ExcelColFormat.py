import glob
import json
import os
import pandas as pd

def change_file_extension(file_path, new_extension):
    file_path_without_extension, current_extension = os.path.splitext(file_path)
    new_file_path = file_path_without_extension + '.' + new_extension
    return new_file_path

class Config:
    def __init__(self,ColName,FormatNum,Col=0):
        self.col=Col
        self.colName=ColName
        self.formatNum=FormatNum

with open(r"./config.json","r",encoding="utf-8") as config:
    configList=[Config(**cfg) for cfg in json.load(config)]

for filename in (glob.glob(os.path.join(r"./inputFile/", '*.xlsx'))+glob.glob(os.path.join(r"./inputFile/", '*.xls'))):
    print(filename)
    df = pd.read_excel(filename)
    for item in configList:
        if(item.colName!="" and item.colName!=None):df[item.colName]=list(map(lambda x:item.formatNum.format(x),df[item.colName]))
        else:df.iloc[:, item.col]=list(map(lambda x:item.formatNum.format(x),df.iloc[:, item.col]))
    df.to_excel(r"./outputFile/"+change_file_extension(os.path.basename(filename),"xlsx"),index=False)