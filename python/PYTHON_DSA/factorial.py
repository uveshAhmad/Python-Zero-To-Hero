def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))






def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact = fact * n
            n = n-1
        return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))



def factorial(n):
       
    res = 1
      
    for i in range(2, n+1):
        res = res* i
    return res
 # Driver Code
num = 5
print("Factorial of", num, "is",
factorial(num))



import math
 
def factorial(n):
    return(math.factorial(n))
 
 
# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))
 
 
 
import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x)



 


