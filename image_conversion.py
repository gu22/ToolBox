# -*- coding: utf-8 -*-
from PIL import Image
import easygui
import os    



user_dir = easygui.fileopenbox()

filename = user_dir

print()
img = Image.open(filename)
user_dir = os.path.basename(filename)
# filename = '.ico'.join(user_dir[0])
img.save(user_dir+'.ico')

