N=int(input("enter the number: "))
sum=0
for i in range(1,N+1):
    if (i%2==0):
        sum=sum+i
        print("sum of the all even numbers between 1 and N",sum)