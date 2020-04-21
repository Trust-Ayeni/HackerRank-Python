#This program is made by Ethyl Joy I. Badiang
import string

nm=list(map(int,input().strip().split()))
n=list(map(int,input().strip().split()))
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))

base=nm[0]
hap=nm[1]
happy=0
for x in range(base):
    for y in range(hap):
        if (n[x]==A[y]):
            happy+=1
        if (n[x]==B[y]):
            happy-=1
print(happy)


