 
# Input: arr[] = {100, 10, 5, 25, 35, 14},
# n = 11
# Output: 9

 
def multiDiv(arr , n):
     sum=1
     for i in arr:
         sum=sum*i
     return (sum%n)  
  

arr= [100, 10, 5, 25, 35, 14]
n= 11
result = multiDiv(arr , n)  
print(result)

  
   