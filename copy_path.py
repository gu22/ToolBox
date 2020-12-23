# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:42:31 2020

@author: glpyz
"""
import easygui
from easygui import *

import shutil
from shutil import copytree

import os

from pathlib import PurePath


destino = easygui.diropenbox()
c = 1

while c <= 3:

    
    origem = easygui.diropenbox()
    
    print(origem,destino)
    
    
    # origem = []
    
    # for i in range(1, 2):
    #     origem.append((easygui.diropenbox()))
        
    # for i in origem:
    #     shutil.copytree(i,destino)
    # shutil.copy(origem,destino)
    
    if  os.path.exists(destino):
        nome = PurePath(origem).name
        destino2 = os.path.join(destino,nome)
        
        shutil.copytree(origem,destino2)
        
        print("Copia realizada - {}".format(destino2))
        
    c +=1