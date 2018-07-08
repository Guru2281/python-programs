num=int(input("Enter 4 digit number   :"))
num2=num
m=1000
res=0
while num>0:
    num1=num%10
    num=num/10
    res+=num1*m
    m=m/10

if res==num2:
    print("No. is palindrome")
else:
    print("No. is not plindrome")

