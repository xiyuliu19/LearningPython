#!/usr/bin/python
import re
phone = "602-343-8747"
num = re.sub(r'-343-8747', "", phone)    
print "The area code is:", num
