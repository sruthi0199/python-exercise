s1=input("Enter a string:")
sum=0
lis=[]
lis=s1.split("-")
for i in range(1,len(lis)):
    lis[i]=int(lis[i])
    sum=sum+lis[i]

print("TOTAL RUN SCORED BY %s:"%lis[0],sum)
for i in range (1,len(lis)):
    if(lis[i]>0):
        print(lis[0]+" is not duct out in %d match"%i)
    else:
        print(lis[0] + " is duct out in %d match" % i)



