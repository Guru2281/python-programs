def fib(num):
    n1=0
    n2=1
    list=[0,1]

    for i in range(num):
        res=n1+n2
        list.append(res)
        n1=n2
        n2=res
    return list

if __name__=="__main__":
    num=int(input("Enter number :"))
    print(fib(num))
