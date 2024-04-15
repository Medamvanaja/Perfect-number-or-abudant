n=int(input())
sum=0
for i in range(1,n,1):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(n,"is perfect number")
elif(sum>n):
    print(n,"is Abudant Number")
else:
    print(n,"is Deficient Number")
