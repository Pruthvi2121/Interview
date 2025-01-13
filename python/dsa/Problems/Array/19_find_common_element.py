










# brute first approch
def solution_m1(arr1,arr2, arr3):
    temp = []
    for i in arr1:
        for j in arr2:
            for k in arr3:
                if i == j == k:
                    temp.append(i)
    return temp



def solution_m2(arr1,arr2, arr3):
    i = 0
    j = 0
    k = 0
    temp = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):

        # if i == j == k    states it is common element
        if arr1[i] == arr2[j] == arr3[k]:
            temp.append(arr1[i])
            i+=1
            j+=1
            k+=1

        #  as arr is sorted then if arr1 ele less than arr2 then that ele is not present on arr2 so increment the i to next ele
        elif arr1[i] < arr2[j]:
            i+=1
        # similarly if the arr2 is smmaller than the arr1 then increment the j
        elif arr2[j] < arr1[i]:
            j+=1

        # we reach here whe  i > j and k < j, j is smaller
        else:
            k+=1
    
    return temp




if __name__ =="__main__":
    arr1 = [-1, 0, 1, 2, -1, -4]
    arr2 =  [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
 
    
    print("method 1 : ", solution_m1([1, 5, 10, 20, 40, 80],  [6, 7, 20, 80, 100] , [3, 4, 15, 20, 30, 70, 80, 120] ) , end="\n\n")
    print("method 2 : ", solution_m2([1, 5, 10, 20, 40, 80],  [6, 7, 20, 80, 100] , [3, 4, 15, 20, 30, 70, 80, 120] ) , end="\n\n")
    # print("method 1 : ", solution_m1(arr2) , end="\n\n")