def index(arr,val):
    count=0
    for i in range(len(arr)):
           if(arr[i]==val):
              count+=i;  
    print(count)
index([1,2,3,4,5],3) 