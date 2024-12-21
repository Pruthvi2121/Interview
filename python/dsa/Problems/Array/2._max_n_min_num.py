"""
Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
        Maximum element is: 9


Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
         Maximum element is: 35

"""



def min_and_max_element_m1(arr):
    """
    iterates through the list .
    assign first elemet as min and max 
    It compares each element with the current minimum and maximum values
    and updates them accordingly.
    """

    min = arr[0]
    max = arr[0]
    arr_len = len(arr)
    
    i = 1
    while i < arr_len:
        
        if arr[i] > max:
            max = arr[i]
        
        if arr[i] < min:
            min = arr[i]

        i+=1
    
    return f"min={min} max={max}"




# by sorting array in ascending and then first element = min and last element = max
def min_and_max_element_m2(arr):
    """
     sort the array accending
     then append first and last element min and max respectively
    """
    arr.sort()
    min = arr[0]
    max = arr[len(arr)-1]
    return f"min={min} max={max}"


if __name__ == "__main__":
    arr = [1, 2, 3, 8, 5, 6]

    print("method 1: ", min_and_max_element_m1(arr), end="\n\n")
    print("method 2: ", min_and_max_element_m2(arr), end="\n\n")
   
   
  
