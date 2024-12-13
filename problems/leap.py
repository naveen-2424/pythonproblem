def lip(n):
    if(n%400==0 or n%100!=0 and n%4==0):
        print("leap year")
    else:
        print("not leap year")    
# n=int(input("Enter the number"))
lip(2020)