import string

n,m=input().split()
sc_ar=set(input().split())
A=set(input().split())
B=set(input().split())
#happy=[(i in A)for i in sc_ar]
#sad=[(i in B)for i in sc_ar]
set1=sc_ar.intersection(A)
set2=sc_ar.intersection(B)
#print(sum(happy)-sum(sad))
print(len(set1)-len(set2))
