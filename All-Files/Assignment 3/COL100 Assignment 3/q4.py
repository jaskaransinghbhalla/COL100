s=input()
if(len(s)<=4):
    if(s[0]==s[len(s)-1]):
        if(s[1]==s[len(s)-2]):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")        