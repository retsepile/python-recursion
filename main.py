result = int(input("Enter your number: "))  # asking the user to input a figure of choice

# defining a function
def factorial(n):
    if n < 0:
        return "You are advised to input a positive number"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# calling the above function
print(factorial(result))