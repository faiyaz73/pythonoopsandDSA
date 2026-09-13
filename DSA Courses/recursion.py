def Recursion(n):   
    if(n == 1 or n == 0):
        return 1
    return n * Recursion(n-1)
while True:
    number = int(input("Enter the Number : "))
    print(Recursion(number))
       
    