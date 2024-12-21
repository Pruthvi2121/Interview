


def bubble_sort(arr):
    n = len(arr)
    i = 0

    while i < n:
 
        j = 1
        while j< n-i:
            if arr[j-1] > arr[j]:
               arr[j-1], arr[j] = arr[j], arr[j-1]
   
            j+=1
            
        i+=1

    



if __name__ =="__main__":
    arr = [4,3,8,2,6,9]
    bubble_sort(arr)