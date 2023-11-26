# short hand If
a=5
b=10
if a > b: print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")  # TernaryTechnicque



# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200
if b > a:
  pass


# ExampleGet your own Python Server
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1



# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print("Finally finished!")


  