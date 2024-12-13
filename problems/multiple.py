def multiplication(arr):
    mul=1
    for i in range(len(arr)):
        mul*=arr[i]
    print(mul)
multiplication([1,2,5])   

def feb(n):
    sum=1
    for i in range(1,n+1):
             sum*=i
    print(sum)            
feb(5)


def feb(n):
    sum=1
    for i in range(1,n+1):
            sum*=i
    return sum                   
print(feb(5))
def even(n):
    i=1
    str1=1
    while(i<=n):
        str1*=i
        i=i+1
    print(str1)
even(5)
