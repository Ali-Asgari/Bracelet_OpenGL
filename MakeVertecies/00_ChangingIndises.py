
# Some indecies are created handy 
# This app will help to find indecies for second object that has same shape with written object
# At first indecies from first object must written in "res" after that programm calculate
#      for next same object and atomaticly put in clipboard


from math import *

start1=340
secMid1=start1+10

res = '''
340,341,342,340,342,343,340,343,344,340,344,345,340,345,346,340,346,347,340,347,348,340,348,349,340,349,350,340,350,341,351,352,353,351,353,354,351,354,355,351,355,356,351,356,357,351,357,358,351,358,359,351,359,360,351,360,361,351,361,352,341,342,352,342,343,353,343,344,354,344,345,355,345,346,356,346,347,357,347,348,358,348,349,359,349,350,360,350,341,361,352,353,342,353,354,343,354,355,344,355,356,345,356,357,346,357,358,347,358,359,348,359,360,349,360,361,350,361,352,341,

    '''
# print(forres.split(','))
xx = res.split(",")
inti1 = []
res2=""
maxim=0
for x in xx:
    # print(x)
    x=x.strip()
    if x!=""and x!="\n":
        res2+=str(int(x)-start1)+','
        inti1.append(int(x)-start1)
        maxim = max(maxim,int(x))
print(inti1)
print(res2)

# start2=340  #if we want set new start for vertecies 
start2=maxim+1
secMid2=start2+10
inti2=inti1.copy()
res2=""
for x in range(len(inti2)):
    res2+=str(inti2[x]+start2)+','
    inti2[x]+=start2
print(res2)
import pyperclip
pyperclip.copy(res2)
spam = pyperclip.paste()
print(max(inti1)+start2+1)