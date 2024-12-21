# Merge 2 sorted arrays without using Extra space.

"""
Merge Two Sorted Arrays Without Extra Space
Last Updated : 11 Nov, 2024
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge both the arrays and rearrange the elements such that the smallest n elements are in a[] and the remaining m elements are in b[]. All elements in a[] and b[] should be in sorted order.

Examples: 

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output: a[] = [2, 2, 3, 4], b[] = [7, 10] 
Explanation: Combined sorted array = [2, 2, 3, 4, 7, 10], array a[] contains smallest 4 elements: 2, 2, 3 and 4, and array b[] contains remaining 2 elements: 7, 10.


Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output: a[] = [1, 2, 3, 5, 8, 9], b[] = [10, 13, 15, 20]
Explanation: Combined sorted array = [1, 2, 3, 5, 8, 9, 10, 13, 15, 20], array a[] contains smallest 6 elements: 1, 2, 3, 5, 8 and 9, and array b[] contains remaining 4 elements: 10, 13, 15, 20.


Input: a[] = [0, 1], b[] = [2, 3]
Output: a[] = [0, 1], b[] = [2, 3] 
Explanation: Combined sorted array = [0, 1, 2, 3], array a[] contains smallest 2 elements: 0 and 1, and array b[] contains remaining 2 elements: 2 and 3.

"""

# step - declare two points 
# step2 - compare the array element with each array pointers    
         # element which less than first array element swap it
# step3  - check for arr2 is sorted ?   
          # create extra funtion which fix the array sort
          # basically swap the higher element to right  eg 6, 4 --> 4, 6

def fixarr2(arr):
    i = 1
    while i < len(arr):
        if arr[i-1] > arr[i]:  
            arr[i-1], arr[i] = arr[i], arr[i-1]
        i+=1

def solution_m1(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j = 0, 0

    while i < n:

        # check arr1[i] element is greater than array[j] element  then swap it
        if arr1[i] > arr2[j]: 
            arr1[i], arr2[j] = arr2[j], arr1[i],  # swap
            fixarr2(arr2)


        i+=1
    return arr1, arr2
    

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]

  
    print("method 1 ", solution_m1(arr1, arr2) , end="\n\n")