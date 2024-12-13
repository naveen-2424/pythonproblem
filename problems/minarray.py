def ismin(arr):
    min=arr[0]
    for i in range(len(arr)):
           if(arr[i]>i):
              min=arr[i]
    print(min)
ismin([1,2,3,4,5])  