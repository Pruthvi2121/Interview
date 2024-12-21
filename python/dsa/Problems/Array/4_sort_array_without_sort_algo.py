"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 2

"""


def sort_without_algo(arr):
    arr_len = len(arr)
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(arr_len):
        if arr[i]==0:
            count_0+=1
        elif arr[i]==1:
            count_1+=1
        else:
            count_2+=1

    return [0]*count_0 + [1]*count_1 + [2]*count_2  
           
        



if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    print("method 1 ", sort_without_algo(arr))
