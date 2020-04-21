test=int(input())
arr=[]
subjects=['Art:','English:','Handwriting:','History:','Math:','P.E.:','Phonics:','Reading:','Religion:','Science/Health:','Spelling:','Vocabulary:']
for x in range(test):
    quarter=int(input())
    stan=int(input())
    grades=list(map(int,input().split()))
    arr.append('CONGRATULATIONS BIMB!')
    if quarter==1:
        quart='1ST'
    elif quarter==2:
        quart='2ND'
    elif quarter==3:
        quart='3RD'
    else:
        quart=str(quarter)+'TH'
    
    state=quart+' QUARTER GRADES'
    arr.append(state)
    for y in range(len(grades)):
        if grades[y]>=stan:
            if grades[y]>=97:
                char='A+'
            elif grades[y]>=93:
                char='A'
            elif grades[y]>=90:
                char='A-'
            elif grades[y]>=87:
                char='B+'
            elif grades[y]>=83:
                char='B'
            elif grades[y]>=80:
                char='B-'
            elif grades[y]>=77:
                char='C+'
            elif grades[y]>=73:
                char='C'
            elif grades[y]>=70:
                char='C-'
            elif grades[y]>=67:
                char='D+'
            elif grades[y]>=63:
                char='D'
            elif grades[y]>=60:
                char='D-'
            elif grades[y]<=59:
                char='F'
            final=subjects[y]+char
            arr.append(final)
for z in range(len(arr)):
    print(arr[z])
                
            
