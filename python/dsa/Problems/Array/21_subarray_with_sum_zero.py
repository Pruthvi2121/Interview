"""
Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. 

Examples:

Input: arr[] = [4, 2, -3, 1, 6]
Output: true
Explanation: 2, -3, 1 is the subarray with a sum of 0.
Input: arr = [4, 2, 0, 1, 6]
Output: true
Explanation: 0 is one of the element in the array so there exist a subarray with sum 0.
Input: arr = [1, 2, -1]
Output: false
Constraints:
1 <= arr.size <= 104
-105 <= arr[i] <= 105
"""


def solution_m1(arr):
    n = len(arr)
    is_subarry = False

    isum = 10000

    i = 0
    k = 0
    while i < n:
        sum = 0
        j = i
        while j < n: 
           sum+=arr[j]
           if sum == 0:
               return True
           j+=1
        i+=1


    return False


def solution_m2(arr):
    prefix_sum_set = set()
    n = len(arr)
    i = 0

    prefix_sum = 0
    while i < n:

        prefix_sum+=arr[i]
         
        # If the prefix sum is 0, we found a subarray with 0 sum
        if prefix_sum == 0:
            return True
        
         # If the prefix sum has been seen before, there is a subarray with 0 sum
        if prefix_sum in prefix_sum_set:
            return True
        
        # Add the current prefix sum to the set
        prefix_sum_set.add(prefix_sum)
        
        i+=1

    return False
    

if __name__ =="__main__":
    arr = [4, 2, -3, 1, 6]


 
    
    print("method 1 : ", solution_m1(arr) , end="\n\n")
    print("method 2 : ", solution_m2(arr) , end="\n\n")