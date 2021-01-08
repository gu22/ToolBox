# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:35:17 2021

@author: GLPYZ
"""


from win10toast import ToastNotifier
toaster = ToastNotifier()
oi = 'ola\nzzz'
toaster.show_toast("",
oi,

duration=10)