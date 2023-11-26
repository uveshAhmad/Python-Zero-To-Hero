list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped_result = zip(list1, list2)   # return tupple 

# Convert the zip object to a list of tuples
result_list = list(zipped_result)

print(result_list)