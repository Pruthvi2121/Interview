"""
56. Merge Intervals
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

def solution_m1(arr):
    n = len(arr)
    i = 1
    arr.sort( key = lambda x:x[0])
   
    while i < n:
        start = 0
        end = 1

        maxi = max(arr[i-1][end], arr[i][end])
        mini = min(arr[i-1][start], arr[ i-1][start])
    
        if arr[i-1][end] >= arr[i][start]:
            arr[i][start] = mini
            arr[i][end] = maxi
            arr.pop(i-1)  
            i=1
            n = len(arr)

            print("updated", arr)
          
        else:
            i+=1

    return arr



if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    interval2 =[[1,4],[4,5]]
    interval3 =[[1,4],[2,3]]

  
    print("method 1 ", solution_m1(intervals) , end="\n\n")
    print("method 1 ", solution_m1(interval2) , end="\n\n")
    print("method 1 ", solution_m1(interval3) , end="\n\n")
    # print("method 2 ", solution_m2([[1,4],[4,5]]) , end="\n\n")