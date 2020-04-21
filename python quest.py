import sys
x=int(input())
str1=[]
for i in range(1,x): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for y in range(0,i):
        str1=str1+str(i)
    sys.stdout.write(str1)
    str1=''
