#!/usr/bin/env python3
l = []
s= open('/home/wlq/project/text/String.txt','r')
for x in s.read():
   if x.isdigit():
        l.append(x)
        
print("".join(l))
 

            
