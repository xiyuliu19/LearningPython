#!/usr/bin/python
import sys
import fileinput
import re
import json

total=[ ]

for line in fileinput.input('/home/xiyuliu/data/Homo_sapiens.GRCh37.75.gtf'):         
    if line.strip()[0] != '#':    
       dic = {}
       column = line.split('\t')
       if column[2] == "gene":
          dic['geneName'] = re.findall('gene_name \"(.*?)\";',column[8])[0]
          dic['chr'] = column[0]
          dic['startPos'] = int(column[3])
          dic['endPos'] = int(column[4])
          total.append(dic)
print("[")
for line in total: 
    print json.dumps(line) + ","
print("]")

fileinput.close( )
