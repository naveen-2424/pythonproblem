def count(arr,val):
    count=0
    for i in range(len(arr)):
           if(arr[i]==val):
              count+=1;  
    print(count)
count([1,2,3,3,4,5,3,3],3) 