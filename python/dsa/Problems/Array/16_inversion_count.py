"""
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104

"""


def solution_m2(arr):
    n = len(arr)
    i=0
    inversion_count = 0
    
    while i < n:
        j=i
        while j<n:
            if arr[i] > arr[j]:
                inversion_count+=1
            j+=1

        i+=1

    return inversion_count




if __name__ =="__main__":
    arr = [2, 4, 1, 3, 5]
    arr2 = [2, 3, 4, 5, 6] 
    arr3 = [10, 10, 10]
    
    print("method 1 ", solution_m2(arr) , end="\n\n")
    print("method 1 ", solution_m2(arr2) , end="\n\n")
    print("method 1 ", solution_m2(arr3) , end="\n\n")