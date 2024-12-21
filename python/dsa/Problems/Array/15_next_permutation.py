"""

Code
Testcase
Test Result
Test Result
31. Next Permutation
Medium
Topics
Companies
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
# flow
# 3 1 4 2 
# here k = 1                 k is the element  which next lement is greater and cyclice of desending arr start eg 4, 2
# swap the k with its next largest elemnt which is 2
#  3 2 4 1  now k = 2
# now rotate the array from k next element ie  k +1 , till end of the array 
#  3 2 1 4  ... is the next permutation



# [3, 1, 4, 2]  here k should be = 1
def solution_m1(arr):
    n = len(arr)
    k = n - 2  # last element by default

    # find k
    i = n - 1
    while i >= 0:
        
        if arr[i-1] < arr[i]:
            k = i-1
            break
        k = i-1
        i-=1
    print("k", k)
    # if k = -1 --> reverse it 
    if k == -1:
        reverse(arr, 0, n-1)
        return arr


    # else  swap the  k with next largest element and reverse the reset form k+1 () to n-1(last elemtn)
    j = n-1
    while j > 0:
        if arr[k] < arr[j]:
            arr[k], arr[j] = arr[j] , arr[k]  # swap
            break
        j-=1
    
    reverse(arr, k+1, n-1)
    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1




if __name__ == "__main__":
    permutation = [3, 1, 4, 2]
    permutation2 = [3,2,1]
  


#  proper decending indecate that permutaion done
#  k is the element from where the element is rotated
  
    print("method 1 ", solution_m1(permutation) , end="\n\n")
    print("method 1 ", solution_m1(permutation2) , end="\n\n")
 