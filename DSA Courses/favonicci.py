def favonicci(n):
    if(n==0):
     return 0
    elif(n==1):
     return 1
    return favonicci(n-1) + favonicci(n-2)
while True:
    number  = int(input("Enter the Number : "))
    print(favonicci(number))