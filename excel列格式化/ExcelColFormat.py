import glob
import json
import os
import pandas as pd

class Config:
    def __init__(self,ColName,FormatNum,Col=0):
        self.col=Col
        self.colName=ColName
        self.formatNum=FormatNum

with open(r"./config.json","r",encoding="utf-8") as config:
    configList=[Config(**cfg) for cfg in json.load(config)]

for filename in glob.glob(os.path.join(r"./inputFile/", '*.xlsx')):
    df = pd.read_excel(filename)
    for item in configList:
        if(item.colName!="" and item.colName!=None):df[item.colName]=list(map(lambda x:item.formatNum.format(x),df[item.colName]))
        else:df.iloc[:, item.col]=list(map(lambda x:item.formatNum.format(x),df.iloc[:, item.col]))
    df.to_excel(r"./outputFile/"+os.path.basename(filename),index=False)