print("Using inbuit function")
s1=input("Enter a string:")
for i in range (len(s1)):
    if(s1[i].islower()):
        print(s1[i],end=" ")
print(" ")
print("Without built in function")
s2=input("Enter a string:")
for i in range(len(s2)):
    if(ord(s2[i])>=97 and ord(s2[i])<=122):
        print(s2[i],end=" ")
