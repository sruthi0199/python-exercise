s1=input("Enter a string:")
txt=s1[::-1]
print(txt)
print("WITHOUT BUILT-IN FUNCTION")
i=len(s1)-1
while(i>=0):
    print(s1[i],end="")
    i=i-1
