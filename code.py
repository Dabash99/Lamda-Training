
Created on Sun Mar  1 21:39:53 2020

@author: Ahmed A. Dabash
"""

key=input("Enter any Text :")
key=key.upper()
print("-".join((lambda txt:[txt[i:i+5]
for i in range (0,len(txt),5)])(key)))
