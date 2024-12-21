"""

Rotate Array by One
Difficulty: BasicAccuracy: 69.6%Submissions: 289K+Points: 1
Given an array arr, rotate the array by one position in clock-wise direction.

Examples:

Input: arr = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
Input: arr = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.

"""


def cyclic_rotate(arr):
    arr_len = len(arr)
    
    if arr_len == 0:
        return
    
    i= arr_len - 1
    while i > 0: 
       arr[i-1], arr[i] = arr[i], arr[i-1]
       
       i-=1
    print(arr)
   

if __name__ == "__main__":
    arr1 =[1, 2, 3, 4, 5]

    print("method 1 ", cyclic_rotate(arr1) , end="\n\n")
   