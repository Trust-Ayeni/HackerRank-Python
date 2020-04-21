def swap_case(s):
    cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    str1=""
    

    for y in range(len(s)):
        test=s[y]
        print("test: "+test)
        for x in range(0,len(cap)):
            if ord(test)>=65 and ord(test)<91:
                str1=str1+chr(ord(test)+32)
                break
            elif((ord(test)>=97)and(ord(test)<123)):
                str1=str1+chr(ord(test)-32)
                #print(",")
                break
            else:
                str1=str1+test
                break
    print(str1)
    return str1

def main():
    x="hEllo"
    y=swap_case(x)
    print("s: "+y)

main()
