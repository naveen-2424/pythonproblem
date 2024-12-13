def issum(arr):
    sum=0
    for i in range(len(arr)):
     sum+=i
    print(sum)
issum([1,2,3,4,5])

def sumof(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print(sum)    
sumof([2,3,4,5,6])



studetname="mena"
subject="social"
mark=99

sentence=f'{studetname} is {subject} {mark} mark scored.'
print(sentence)

output:mena is social 99 mark scored.


Bharathwaj|Guduvancherry


data='Naveen|Erode'
atpos=data.find('|')
print(atpos)
secondpart=data[atpos + 1: len(data)]
print(secondpart)

data='Naveen|Erode'
print(data.split("|")[1])
# print(data.split(" "))

data = 'From stephen.marquard@ gmail.com Sat Jan  5 09:14:16 2008'
start=data.split(" ")
print(start[2])
print(start[7])


data = 'From stephen.marquard@ gmail.com Sat Jan  5 09:14:16 2008'