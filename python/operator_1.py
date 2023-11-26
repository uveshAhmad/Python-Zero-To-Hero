print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole numberx = 15




print(False == 0)
print(True == 1)
 
print(True + True + True)
print(True + False + False)
 
print(None == 0)
print(None == [])

print(True or False)
print(False and True)
print(not True)
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")
for i in 'geeksforgeeks':
    print(i, end=" ")
 
print("\r")
print(' ' is ' ')
print({} is {})




for i in range(10):
 
    print(i, end=" ")
    if i == 6:
        break
 
print()   # For next Line
i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end=" ")
 
    i += 1


i = 20
if (i == 10):
    print("i is 10")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")