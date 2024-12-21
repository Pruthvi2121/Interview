"""
Input: arr[] = {1, 4, 3, 2, 6, 5}  
Output: {5, 6, 2, 3, 4, 1}
Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.


Input: arr[] = {4, 5, 1, 2} 
Output: {2, 1, 5, 4}
Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

"""



#  Method 1
def reverse_array_m1(arr):
    """
        Reverse wit appending 
        initilaize empty temp array []
    """

    arr = [1,2,3,4,5,6]
    arr_len = len(arr)
    temp = []
    for i in range(arr_len ):
        temp.append(arr[(arr_len -1) - i])

    return temp



#  Method 2
def reverse_array_m2(arr):
    """
        Reverse without appending 
        initilaize temp array with same size of the given array
    """
    arr = [1,2,3,4,5,6]
    arr_len = len(arr)
    temp = [0] * arr_len  
    for i in range(arr_len ):
        temp[i] = arr[(arr_len -1) - i]
    
    return temp




#  Method 3

def reverse_array_m3(arr):
    """
        Reverse with python slicing  
    """
    return arr[::-1]


#  Method 

def reverse_array_m4(arr):
    """
        Reverse with two pointers 
    """
    
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left pointer
        left += 1
      
        # Decrement the right pointer
        right -= 1
    
    return arr
        






    



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]

    print("method 1 ", reverse_array_m1(arr))
    print("method 2 ", reverse_array_m2(arr))
    print("method 3 ", reverse_array_m3(arr))
    print("method 4 ", reverse_array_m4(arr))
   
  
    # for i in range(len(arr)):
    #     print(arr[i], end=" ")