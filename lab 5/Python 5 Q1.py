n = int(input("Enter a number between 1 -20: "))
i=1
if n<21 and n>0:
    while i<=n:
        a=1
        while a<=20:
            print(i,"x", a,"=", a*i) 
            a= a+1
        i= i+1
else:
    print("Invalid input")