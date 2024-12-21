"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5


"""


def move_negative_to_oneside_m1(arr):
    i = 0
    positive = []
    negative = []
    while i < len(arr):
        if arr[i] > 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])

        i+=1
    return negative + positive


def move_negative_to_oneside_m2(arr):
    arr.sort()
    return arr
    

def move_negative_to_oneside_m3(arr):
    """
    Function to move all negative numbers to one side of the array using the Dutch National Flag Algorithm.
    The algorithm partitions the array in-place by swapping elements to arrange all negative numbers
    on the left side and all non-negative numbers on the right side.
    """
    left = 0  # Pointer to the beginning of the array (starting from the left)
    right = len(arr) - 1  # Pointer to the end of the array (starting from the right)
    
    # Run the loop until the left pointer is less than the right pointer
    while left < right:
        
        # If the element at the 'left' pointer is negative, we move the pointer to the right
        if arr[left] < 0:
            left += 1  # Move left pointer to the right, as this element is already in the correct place

        # If the element at the 'right' pointer is non-negative, we move the pointer to the left
        elif arr[right] >= 0:
            right -= 1  # Move right pointer to the left, as this element is also in the correct place

        # Swap if left is non-negative and right is negative
        else:
            # Swap the elements at the 'left' and 'right' pointers to move the negative element to the left
            arr[left], arr[right] = arr[right], arr[left]
            # After swapping, increment the left pointer and decrement the right pointer to continue the process
            left += 1
            right -= 1
    
    # Return the modified array with negative numbers on the left side and non-negative on the right side
    return arr

 

if __name__ == "__main__":
    arr = [1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]
    print("method 1 ", move_negative_to_oneside_m1(arr) , end="\n\n")
    print("method 2 ", move_negative_to_oneside_m2(arr) , end="\n\n")
    print("method 3 ", move_negative_to_oneside_m3(arr) , end="\n\n")
