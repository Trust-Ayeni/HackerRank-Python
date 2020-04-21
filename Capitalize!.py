#This program is created by Ethyl Joy I. Badiang
import string
def solve(s):
    alpa="abcdefghijklmnopqrstuvwxyz"
    cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if(s[0]!=" "):
        for y in range(26):
               if s[0]==alpa[y]:
                   s=cap[y]+s[1:]
        
    for x in range(len(s)-1):
        if(s[x]==" " and s[x+1].islower()):
           for y in range(26):
               if s[x+1]==alpa[y]:
                   s=s[:x+1]+cap[y]+s[x+2:len(s)]
    print(s)


    
name=input()

solve(name)

#print(new)
