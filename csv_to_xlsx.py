# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:42:33 2020

@author: GLPYZ
"""


import pandas as pd
import easygui as eg
import datetime
import chardet
import os

data = datetime.datetime.now()
data = (str(data.strftime("%y.%m.%d_%H.%M.%S")))

print(f'Iniciou: {data}')

file_raw = eg.fileopenbox()
path = os.path.dirname(file_raw)
with open(file_raw, 'rb') as f:
    result = chardet.detect(f.read()) 
# with open (file_raw,'r',encoding='utf-8') as file:
#     read_file = pd.read_csv(file)
#     read_file.to_excel("OTD - {}".format(data),index=None,header=True)

read_file = pd.read_csv(file_raw,encoding =result['encoding'],sep="\t")
name = os.path.join(path,("OTD - {}.xlsx".format(data)))
read_file.to_excel(name,index=None,header=True)
