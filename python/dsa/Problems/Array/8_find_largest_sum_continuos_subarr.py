"""
Kadane's Algorithm
Difficulty: MediumAccuracy: 36.28%Submissions: 1MPoints: 4
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
Constraints:
1 ≤ arr.size() ≤ 105
-109 ≤ arr[i] ≤ 104


"""
# https://www.youtube.com/watch?v=w4W6yya1PIc


    # step-1 sum = sum + arr[i]   //  sum of element

    # step-2 maxi = update    // update the maximum sum  between  maxi and sum

    # step-3 if sum < 0 :   (negative sum)  then update the sum=0
    #          sum = 0  

def largest_sum_of_continous_subarry_m1(arr):
    
    maxi=arr[0]
    i=0
    sum = 0
    while i < len(arr):

        # step - 1  add the element to sum
        sum +=arr[i]

        # step - 2 update the maxi
        maxi =  max(maxi, sum)

        # step -3 if the sum is negative update the sum to 0 zero
        if sum < 0:
            sum=0

        i+=1
    return maxi



def largest_sum_of_continous_subarry_m2(arr):  
    i = 0
    max_sum = float('-inf')  # Start with negative infinity to account for all negative sums.
    
    # Outer loop: iterate over each possible start index `i` of the subarray.
    while i < len(arr):
        sum = 0   # Initialize the sum of the subarray starting at `i`.
        j = i     # j is the start point of the subarray

        while j < len(arr):  # iterate over i'th subarray  
            sum+=arr[j]
            j+=1

            if sum > max_sum:    # If the current subarray sum is greater than the previous maximum sum, update it.
                max_sum = sum
        i+=1

    return max_sum



if __name__ == "__main__":
    arr1 = [-2, -4, -1]

    print("method 1 ", largest_sum_of_continous_subarry_m1(arr1) , end="\n\n")
    print("method 2 ", largest_sum_of_continous_subarry_m2(arr1) , end="\n\n")
   