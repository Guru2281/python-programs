lower=input("Enter the lower range:")
upper=input("Enter the upper range:")
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)
