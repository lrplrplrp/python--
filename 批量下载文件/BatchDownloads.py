import glob
import json
import os
import requests
from urllib.parse import urljoin
import pandas as pd

pathConfig=""
extensionConfig=""
urlConfig=""
fileNameConfig=""

with open(".//config.json","r",encoding="utf-8") as config:
    data=json.load(config)
    pathConfig=data["path"]
    extensionConfig=data["extension"]
    urlConfig=data["url"]
    fileNameConfig=data["fileName"]

for filename in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.xlsx')):
    # 读取Excel文件
    df = pd.read_excel(filename)
    path=pathConfig#'.//png//'
    for index, row in df.iterrows():
        url=row[urlConfig]
        name=row[fileNameConfig]
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                tempstr=extensionConfig
                tempNum=0
                while os.path.exists(path+name+tempstr):
                    tempNum=tempNum+1
                    tempstr=f'({str(tempNum)}){tempstr}'
                with open(path+name+tempstr, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {path+name+tempstr}")
            else:
                print(f"Failed to download {path+name+tempstr}")
        except:
            print(f'Connect error {path+name+tempstr}')