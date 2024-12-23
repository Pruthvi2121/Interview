"""
Merge Sort is a divide-and-conquer algorithm used to sort an array. It works by:

Dividing the array into two halves.
Recursively sorting each half.
Merging the sorted halves to create a fully sorted array.
Steps:
Split the array into two halves until each subarray has one element (a single element is already sorted).
Merge the subarrays back together, sorting them as you combine them.
Example:
For an array like [38, 27, 43, 3, 9, 82, 10]:

Divide: [38, 27, 43] and [3, 9, 82, 10]
Sort each half: [27, 38, 43] and [3, 9, 10, 82]
Merge them back into the sorted array: [3, 9, 10, 27, 38, 43, 82]
Time Complexity:
O(n log n), where n is the number of elements in the array.
Space Complexity:
O(n), due to the extra space needed for the merged arrays.
Merge Sort is efficient for large datasets because its time complexity remains O(n log n) even in the worst case.


"""
def merge(arr, left, mid, right):
    n = (mid - left) + 1
    m = (right - mid)
 
    arr_left = [0]*n
    arr_right = [0]*m

    # fill arr_left
    i=0
    while i < n:
        arr_left[i] = arr[left +  i]
        i+=1

    # fill arr_right
    j=0
    while j < m:
        arr_right[j] = arr[mid+1 +  j]
        j+=1

    
    i=0
    j=0
    k=left
    while i<n and j<m:
        
        if arr_left[i] < arr_right[j]:
            arr[k]=arr_left[i] 
            i+=1
        else:
            arr[k]=arr_right[j] 
            j+=1

        k+=1

    while i < n:
        arr[k]=arr_left[i]
        i+=1
        k+=1

    while j < m:
        arr[k]=arr_right[j]
        j+=1
        k+=1


def mergeSort(arr, left, right):

    if left < right:

        mid = (left + right) // 2
        # divide left half
        mergeSort(arr, left, mid)

        # divide right half
        mergeSort(arr, mid+1, right)
    
        merge(arr, left, mid, right)
    else:
        return arr


if __name__ == "__main__":
   
    arr = [3, 1, 4, 2]
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
 