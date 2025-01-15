"""
Maximum Product Subarray
Difficulty: MediumAccuracy: 18.09%Submissions: 422K+Points: 4
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10



"""
def solution_m1(arr):
    n = len(arr)
    i = 0
    max_product = 0
    while i < n:
        j = i
        prod = 1
        while j < n:
            prod*=arr[j]
            max_product = max(max_product, prod)
            j+=1
        i+=1
    return max_product

def solution_m2(arr):
   
    ans = arr[0]
    left_prod = 1
    right_prod = 1
    n = len(arr)
    i=0
    while i< n:
        # if zero
        left_prod = 1 if left_prod == 0 else left_prod
        right_prod = 1 if right_prod == 0 else right_prod

        # update
        left_prod *= arr[i]
        right_prod *=  arr[ n-i-1 ]

        ans = max(ans, max(left_prod, right_prod))
        
        i+=1
    return ans

    

if __name__ =="__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    arr1 = [-1,-2,-3,0]
    arr2 = [2, 3, 4] 
    
    # print("method 1 : ", solution_m1(arr) , end="\n\n")
    print("method 1 : ", solution_m1(arr1) , end="\n\n")
    # print("method 1 : ", solution_m1(arr2) , end="\n\n")

    # print("method 2 : ", solution_m2(arr) , end="\n\n")
    print("method 2 : ", solution_m2(arr1) , end="\n\n")
    # print("method 2 : ", solution_m2(arr2) , end="\n\n")



