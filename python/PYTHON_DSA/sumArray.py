def arrSum(list):
 sum=0   
 for i in list:
    sum=sum+i  
 return sum        


list = [1,2,3,4,5,6]
result = arrSum(list)
print(result)


 
# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]
 
    # calculating length of array
    n = len(arr)
    # calling function ans store the sum in ans
    ans = arrSum(arr)
    # display sum
    print('Sum of the array is ', ans)
    
    
    
    
arr = [12, 3, 4, 15] 
# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)
# display sum
print('Sum of the array is ', ans)





def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum
#Examples
arr = [1, 2, 3]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 6
arr = [15, 12, 13, 10]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 50