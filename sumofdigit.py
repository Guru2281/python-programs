num1=int(input("Enter number  :"))
sum=0
while num1>0:
    num2=num1%10
    num1=num1/10
    sum+=num2

print(sum)
