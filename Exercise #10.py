s1=input("Enter a sentence:")
lis=[]
lis=s1.split(" ")
temp=lis[0]
lis[0]=lis[1]
lis[1]=temp
s1=" ".join(lis)
print(s1)