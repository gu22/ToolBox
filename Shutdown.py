# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:49:56 2021

@author: gusan
"""

import os
import time
import datetime
import easygui
import subprocess
import sys
from win10toast import ToastNotifier

aviso = ToastNotifier()

# tempo = easygui.enterbox("Quanto tempo?\n*em minutos")
tempo = input('Quanto tempo? *em minutos: ')
print('\n')

agora = str(datetime.datetime.fromtimestamp(time.time()).strftime(r'%H:%M:%S'))

while True:
    try:
        tempo = int(tempo)
        shut = tempo * 60
        print('é int')
        break
    except:
        print ('é string')
        break

tipo = type(tempo)

if tipo is int:
    
    msg1 = f"Agora sao: {agora}\nSistema ira encerrar em {tempo} min"
    # aviso.show_toast('Desligando',msg1,duration=5)
    # os.system(f'shutdown -s -t {shut}')
    subprocess.call(f'shutdown -s -t {shut}')
else:
    
    # msg0 = "Shutdown cancelado"
    # aviso.show_toast('Desligando',msg0,duration=3)
    subprocess.call('shutdown -a')
    
sys.exit()