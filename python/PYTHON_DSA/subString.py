MyString1 = "A geek in need is a geek indeed"
 
if "need" in MyString1:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")
    
    
    
    string = "geeks for geeks"  # or string=input() -> taking input from the user
substring = "geeks"  # or substring=input()
 
# splitting words in a given string
s = string.split()
 
# checking condition
# if substring is present in the given string then it gives output as yes
if substring in s:
    print("yes")
else:
    print("no")
    
    
    
s="geeks for geeks"
s2="geeks"
print(["yes" if s2 in s else "no"])

    
    