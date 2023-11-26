import itertools 
 
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]
 
# iterates over 3 lists and executes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for (a, b, c) in zip(num, color, value):
     print (a, b, c)
    #  Output:
# 1 red 255
# 2 while 256