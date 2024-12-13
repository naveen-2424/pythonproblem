def maxin(arr):
    max=arr[0]
    for i in range(len(arr)):
           if(arr[i]>i):
              max=arr[i]
    print(max)
maxin([1,2,3,4,5])  