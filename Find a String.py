def count_substring(string, sub_string):
    num=0
    for x in range(len(string)):
        if(string[x:x+len(sub_string)]==sub_string):
            num+=1
    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
