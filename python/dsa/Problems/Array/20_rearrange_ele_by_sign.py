"""
Rearrange Array Elements by Sign
Last Updated : 08 Nov, 2024
Given an array arr[] of size n, the task is to rearrange it in alternate positive and negative manner without changing the relative order of positive and negative numbers. In case of extra positive/negative numbers, they appear at the end of the array.

Note: The rearranged array should start with a positive number and 0 (zero) should be considered as a positive number.

Examples: 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {1, -4, 2, -1, 3, 4}


Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

"""



def solution_m1(arr):
    pos = []
    neg = []
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
        i+=1

    temp = []
    
    i = 0
    j = 0
    while i < len(neg) and j < len(pos):

        temp.append(neg[i])
        temp.append(pos[j])
        i+=1
        j+=1
    
    while i < len(neg):
        temp.append(neg[i])
        i+=1
      
    while j < len(pos):
        temp.append(pos[j])
        j+=1
    return temp

        
    

def solution_m2(arr):
    n = len(arr)

    left = 0
    right = n - 1

    while left < right:
        if arr[left] < 0 and arr[right] > 0:
            # swap
            arr[left] , arr[right] = arr[right] , arr[left] 
        left+=1
        right-=1
    print("arr", arr)
        


if __name__ =="__main__":
    arr = [1, 2, 3, -4, -1, 4]
    arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

 
    
    # print("method 1 : ", solution_m1(arr) , end="\n\n")
    # print("method 1 : ", solution_m1(arr2) , end="\n\n")

    print("method 2 : ", solution_m2(arr2) , end="\n\n")
 
    # print("method 1 : ", solution_m1(arr2) , end="\n\n")