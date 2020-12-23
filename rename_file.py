# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:16:36 2020

@author: GLPYZ
"""

import pandas as pd
import easygui as eg
import os
import shutil
import datetime


extensao = 'xlsx'
path = eg.diropenbox()
# name_path = os.path.dirname(path)

files = os.listdir(path)

data = datetime.datetime.now()
data = (str(data.strftime("%d-%m")))

for i in files:
    arq = os.path.join(path,i)
    
    base = pd.read_excel(arq)
    
    try:
        transporte = base.iloc[0]['Transportadora']
        print (transporte)
    except:
        print('Pulando  '+arq)
        continue
    
    name = 'OTD - {}_{}.{}'.format(transporte,data,extensao)
    os.rename(arq,(os.path.join(path,name)))

print(files)