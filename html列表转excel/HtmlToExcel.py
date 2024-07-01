import json
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
import os 
import glob

def change_file_extension(file_path, new_extension):
    file_path_without_extension, current_extension = os.path.splitext(file_path)
    new_file_path = file_path_without_extension + '.' + new_extension
    return new_file_path

class Config:
    def __init__(self, colName,lable,className, prop):
        self.lable = lable
        self.colName = colName
        self.className = className
        self.prop = prop

configList=[]
inputFile=r"./inputFile/"
outputFile=r"./outputFile/"

with open(r"./config.json","r") as config:
    configList=[Config(**cfg) for cfg in json.load(config)]
#os.path.dirname(os.path.abspath(__file__))
for filename in glob.glob(os.path.join(inputFile, '*.txt')):
    with open(filename, 'r',encoding='utf-8') as file:
        text = file.read()
        # 使用BeautifulSoup解析HTML表格
        soup = BeautifulSoup(text, 'lxml')
        df=pd.DataFrame()
        temp=[]
        for config in configList:
            if(config.className=="" or config.className==None):
                temp=soup.find_all(config.lable)
            else:
                temp=soup.find_all(config.lable,class_=config.className)
            if(config.prop!="string"):
                df[config.colName]= list(map(lambda item:item.get(config.prop),temp))
            else:
                df[config.colName]= list(map(lambda item:item.string,temp))
        df.to_excel(outputFile+change_file_extension(os.path.basename(filename), 'xlsx'), index=False)

 
