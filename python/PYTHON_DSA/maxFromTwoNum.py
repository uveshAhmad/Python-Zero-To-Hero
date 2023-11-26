def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(maximum(a, b))




a = 2
b = 4
maximum = max(a, b)
print(maximum)




a = 2
b = 4
# Use of ternary operator
print(a if a >= b else b)




a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')



a=2;b=4
x=[a if a>b else b] 
print("maximum number is:",x)




a = 2
b = 4
x=[a,b]
x.sort()
print(x[-1])









