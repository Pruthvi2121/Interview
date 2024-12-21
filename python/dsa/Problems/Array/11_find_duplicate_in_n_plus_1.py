"""
287. Find the Duplicate Number
Medium
Topics
Companies
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

"""




def solution_m1(arr):
    n = len(arr)
    
    for i in range(n):
        index = abs(arr[i])

        if arr[index] < 0:
            return index
        
        arr[index] = -arr[index]
        
    print(arr)
    return -1


if __name__ == "__main__":
    arr = [1,3,4,2,2]

  
    print("method 1 ", solution_m1(arr) , end="\n\n")