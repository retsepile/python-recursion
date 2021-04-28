# defining a function
def recursion_fibo(x):
     if x <= 1:
         return x
     else:
         return recursion_fibo(x - 1) + recursion_fibo(x - 2)

# telling user to enter any number they choose to enter
x = int(input("Enter any number: "))

if x <= 0:
    print("Please enter a positive figure")
else:
    print("Fibonacci sequence: ")
    for i in range(x):
        print(recursion_fibo(i), end= " ")