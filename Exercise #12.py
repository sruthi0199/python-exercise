s1=input("Enter a string:")
ch=input("Enter a character:")
lis=[]
if(ch in s1):
    print("First occurence:",s1.index(ch))
    for i in range(len(s1)):
        if(s1[i]==ch):
            lis.append(i)
    print("List of all indexes where %s occurs:"%ch,lis)
else:
    print("Character is not found in the string")
