n=int(input("Enter number:"))
i=1
count=0
for x in range(i,n):
    if(n%x)==0:
         count=count+1
if(count>2):
    print("not prime number")
else:
    print("prime")