s1=input("Enter a string:")
dup=[]
for i in s1:
    if s1.count(i)>1:
        if i not in dup:
            dup.append(i)
for i in dup:
    print(i)
for i in dup:
    print("The number of times",i," is repeated:",s1.count(i))


