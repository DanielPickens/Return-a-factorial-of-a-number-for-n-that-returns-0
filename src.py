def factorial(n):
       
    if n == 0:
        return 0
      
    return n * factorial(n-1)
   
# Driver Code
num = 0;
print("Factorial of", num, "is",
factorial(num))
