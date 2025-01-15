"""
Longest Consecutive Subsequence
Difficulty: MediumAccuracy: 33.0%Submissions: 341K+Points: 4
Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.
Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105


"""

def solution_m1(arr):

    my_dict = {i:False for i in arr }
    
    i = 0
    n = len(arr)
    longest_len = 0
    while i < n:
        
        # check forward
        current_length = 1
        next_num = arr[i] + 1
        while my_dict.__contains__(next_num ) and my_dict.get(next_num) == False:
            my_dict[next_num] = True
            current_length+=1
            next_num+=1


        # check backword
        prev_num = arr[i] - 1
        while my_dict.__contains__(prev_num) and my_dict.get(prev_num) == False:
            my_dict[prev_num] = True
            current_length+=1
            prev_num-=1

        longest_len = max(longest_len, current_length)
        i+=1
    return longest_len



if __name__ =="__main__":
    arr = [100,4,200,1,3,2]
    print("method 1 : ", solution_m1(arr) , end="\n\n")
    
    pass
