test=int(input())
subjects=['Art:','English:','Handwriting:','History:','Math:','P.E.:','Phonics:','Reading:','Religion:','Science/Health:','Spelling:','Vocabulary:']
for x in range(test):
    quarter=int(input())
    stan=int(input())
    grades=list(map(int,input().split()))
    print('CONGRATULATIONS BIMB!')
    if quarter==1:
        quart='1ST'
    elif quarter==2:
        quart='2ND'
    elif quarter==3:
        quart='3RD'
    else:
        quart=str(quarter)+'TH'
    
    print(quart,'QUARTER GRADES')
    for y in range(len(grades)):
        if grades[y]>=stan:
            if grades[y]>=98:
                char='A+'
            elif grades[y]>=93:
                char='A'
            elif grades[y]<93:
                char='A-'
            print(subjects[y],char)
                
            
