n=int(input())
code=''
for x in range (n):
    ray=list(map(int,input().split()))
    char=45-sum(ray)
    code=code+str(char)
print(code)
