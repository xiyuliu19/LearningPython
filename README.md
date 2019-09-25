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
vi gene_names.py
```python

