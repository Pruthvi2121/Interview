
"""

Two sum -Pairs with 0 Sum
Difficulty: EasyAccuracy: 31.49%Submissions: 461K+Points: 2
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

Constraints:
3 <= arr.size <= 105
-105 <= arr[i] <= 105

"""




def solution_m1(arr):
    n = len(arr)
    i = 0
    temp = set()
    while i < n:
        j = 0
  
        while j < n:
            if (arr[i] + arr[j]) == 0:
                if arr[i] < arr[j] and  arr[i] != arr[j]:
                    
                    temp.add( tuple([ arr[i] , arr[j] ]))
                if arr[i] > arr[j] and  arr[i] != arr[j]:
                  
                    temp.add(tuple([ arr[j] , arr[i]]))
            j+=1
        i+=1
    return list(temp)


if __name__ =="__main__":
    arr1 = [-1, 0, 1, 2, -1, -4]
    arr2 =  [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
 
    
    print("method 1 : ", solution_m1(arr1) , end="\n\n")
    print("method 1 : ", solution_m1(arr2) , end="\n\n")