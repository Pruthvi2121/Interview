"""
Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.

Examples

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: 2
Explanation: We need to consider only distinct. So count is 2.


"""


# Union of two arrays is an array having all distinct elements 
# that are present in either array



def union_count_m1(arr1, arr2):
    arr1_len, arr2_len =  len(arr1), len(arr2)
    i, j = 0, 0
    union_list = []
    intersection_list = []
    while i < arr1_len  and j < arr2_len:
        
        if arr1[i] < arr2[j]:
            union_list.append(arr1[i])
            i+=1

        elif arr2[j] < arr1[i]:
            union_list.append(arr2[j])
            j+=1
        
        else:
            union_list.append(arr1[i])
            intersection_list.append(arr1[i])
            i+=1
            j+=1
    
    while i < arr1_len:
        union_list.append(arr1[i])
        i+=1
        
    while j < arr2_len:
        union_list.append(arr2[j])
        j+=1
        
    print("union list :", union_list)
    print("intersection :", intersection_list)



def union_count_m2(arr1, arr2):
    distict_arr1 = set(arr1)
    distict_arr2 = set(arr2)
    union = distict_arr1 | distict_arr2
    return len(union)


def union_count_m3(arr1, arr2):
    union_set = set()

    for i in arr1:
        union_set.add(i)

    for j in arr2:
        union_set.add(2)

    return len(union_set)




if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [1, 2, 3]
    print("method 1 ", union_count_m1(arr1, arr2) , end="\n\n")
    # print("method 2 ", union_count_m2(arr1, arr2) , end="\n\n")
    # print("method 3 ", union_count_m3(arr1, arr2) , end="\n\n")
  
