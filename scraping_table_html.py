# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:54:58 2021

@author: GLPYZ
"""

from urllib.request import urlopen
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import easygui
import re
import pandas as pd
from IPython.display import display,HTML
from tabulate import tabulate

file =easygui.fileopenbox()

# extract = urlopen('file:///C:/Users/Public/GLPYZ/1.%20PROGRAMA%C3%87%C3%83O/SAA/br_hmtl.html')
# print(extract)

# htmlparser = etree.HTMLParser()


# tree = etree.parse(extract,htmlparser)

# table = tree.xpath('//*[@id="tableEntregaNfs"]')


# result = etree.tostring(table,pretty_print=True,method='html')

with open (file,"r",encoding=('utf-8')) as out:
    
    soup = BeautifulSoup(out,"lxml")
    
    tablesoup = soup.find_all('table',attrs={'id':'tableEntregaNfs'})
    
    print(len(tablesoup))
    
    table = tablesoup[0]
    
    body = table.find_all('tr')
    head = body[0]
    
    body_rows = body[1:]
    
    headings = []
    
    for item in head.find_all('th'):
        item = (item.text).rstrip("\n")
        headings.append(item)
        
    print(headings)
    
    all_rows = []
    
    for row_num in range(len(body_rows)):
        row=[]
        
        for row_item in body_rows[row_num].find_all('td'):
            
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            
            row.append(aa)
            
        del (row[4:6])    
        all_rows.append(row)
        
    br = pd.DataFrame(data=all_rows,columns=headings)
    
    with open("brasil.html","w",encoding=('utf-8')) as wr:
        wr.write((br.to_html()))
    
    