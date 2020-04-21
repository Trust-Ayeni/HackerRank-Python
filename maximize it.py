 #maximize it
from itertools import count
lines,mod=map(int,input().split())
great,tot=[],0
for x in count(0):
    if x<lines:
        line=list(map(int,input().split()))
        tot=tot+(max(line)*max(line))
    else:
        break
print(tot%mod)
