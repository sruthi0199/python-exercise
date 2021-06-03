print("ENTER A STRING")
s1=input()
c1=0
c2=0
c3=0
for i in range(len(s1)):
    if(s1[i].isdigit()):
        c1=c1+1
    elif(s1[i].islower()):
        c2=c2+1
    elif(s1[i].isupper()):
        c3=c3+1
print("NUMBER OF DIGITS IN THE STRING:",c1)
print("NUMBER OF LOWERCASE CHARACTERS IN THE STRING:",c2)
print("NUMBER OF UPPERCASE CHARACTERS IN THE STRING:",c3)