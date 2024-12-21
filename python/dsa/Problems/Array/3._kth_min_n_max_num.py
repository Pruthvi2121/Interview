"""
Given an array arr[] and an integer k where k is smaller than the size of the array, 
the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.
Expected Time Complexity: O(n+(max_element) )
Expected Auxiliary Space: O(max_element)

Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n

"""


def kth_min_element_m1(arr, k):
    """
    sort the array in acending
    then find the kth element 
    """
    arr.sort()   
    return arr[k-1]


    


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print("method 1 ", kth_min_element_m1(arr, k=3))

   