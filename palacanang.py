import math
import sys
test=int(input())
area=0
arr=[]

for x in range(test):
    state=''
    x1=0
    y1=0
    x3=0
    y3=0
    x0,y0,x2,y2=map(int,input().split())
    p,b=map(float,input().split())

    if abs(x2-x0)==abs(y2-y0) and (x0==x2 or y0==y2) :
        dist=2/math.sqrt(2)*abs(y0)
        area=round(dist**2)
        per=dist*4
        x1=x2
        y1=y0
        x3=x0
        y3=y2
        
    elif x2+x0==y2+y0 and x2+x0==0 and (x0==x2) :#(0,3) & (0,-3)
        side=2/math.sqrt(2)*abs(y2)
        area=round(side**2)
        per=side*4
        x1=y0
        y1=x0
        x3=y2
        y3=x2
        
    elif x2+x0==y2+y0 and x2+x0==0 and (y0==y2) :#(3,0) & (-3,0)
        side=2/math.sqrt(2)*abs(x2)
        area=round(side**2)
        per=side*4
        x1=y0
        y1=x2
        x3=y2
        y3=x0
        
    elif x2+x0==y2+y0 and x2+x0==0:#(-1,-1) (1,1)
        side=abs(y0)+abs(y2)
        area=side**2
        per=side*4
        if x0==y0 or x2==y2:
            x1=x0
            y1=y2
            x3=x2
            y3=y0
        else:
            x1=x2
            y1=y0
            x3=x0
            y3=y2
        
   
    elif x2+x0==y2+y0 and x2+x0==0 and (y0==y2 or x0==x2):# -4 0 4 0
        side=2/math.sqrt(2)*abs(x2)
        area=round(side**2)
        per=side*4
        x1=y2
        y1=x2
        x3=y0
        y3=x0

    
    
        
    cost=(area*p)+(per*b) 
    state=str(cost)+' '+str(x1)+' '+str(y1)+' '+str(x3)+' '+str(y3)
    arr.append(state)
for x in range(len(arr)):
    print(arr[x])
