# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:30:25 2020

@author: GLPYZ
"""

import base64
import getpass
# from getpass import getpass

import sys

pword = getpass.getpass(prompt = "word: ",stream=sys.stderr)
pword = (base64.b64encode(pword.encode("rot13")))
# pword = (base64.b64encode(pword.encode("utf-8")))
   