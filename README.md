# LearningPython
There are 3 scripts
***
## 1.circumference.py
*This script assigns pi to 3.14159 and prints the circumference of a circle of radius 3.*<br>
vi circumference.py <br>
```python
#!/usr/bin/python

pi= 3.14159
r = 3
print ("The circumference of a circle of radius " + str(r) + " is: " + str(2*pi*r))
```
./circumference.py <br>
Prints: **The circumference of a circle of radius 3 is: 18.84954** <br>
***
## 2.areaCode.py
*This script uses regular expressions to extract the area code.*
vi areaCode.py <br>
```python
#!/usr/bin/python
import re
phone = "602-343-8747"
num = re.sub(r'-343-8747', "", phone)
print "The area code is:", num
```
./areaCode.py <br>
Prints: **The area code is: 602** <br>
***
## 3.gene_names.py
*This script takes a gtf file called **Homo_sapiens.GRCh37.75.gtf.gz** as an argument, and spits out the gene_name, the chromosome (the first column), the starting position (the fourth column), and the ending position (the fifth column) for only those columns where the third column is “gene”.* <br>
I create a new directory called data within my home directory. <br> 
wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz <br>
gunzip Homo_sapiens.GRCh37.75.gtf.gz <br>
head ~/data/Homo_sapiens.GRCh37.75.gtf #see the start of the file (#!genome-build GRCh37.p13) <br>
vi gene_names.py
```python
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
```
./gene_names.py ~/data/Homo_sapiens.GRCh37.75.gtf <br>
**Here, I can have all the information required and the format is totally same as the professor showed.** <br>
***
