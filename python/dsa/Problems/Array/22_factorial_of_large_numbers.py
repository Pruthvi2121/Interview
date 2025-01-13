"""
Factorials of large numbers
Difficulty: MediumAccuracy: 36.57%Submissions: 156K+Points: 4
Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [1]
Explanation: 1! = 1 
Constraints:
1 ≤ n ≤ 103


"""
def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left +=1
        right -=1


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)


def solution_m1(n):
    fact = factorial(n)
    output = []
    digit = fact

    while digit > 0:
       
        rem = digit % 10
        output.append(rem)
        digit = digit//10

    # reverse
    reverse(output)
    return output

    

if __name__ =="__main__":
    arr = [4, 2, -3, 1, 6]
 
    
    print("method 1 : ", solution_m1(5) , end="\n\n")
    print("method 1 : ", solution_m1(10) , end="\n\n")
    print("method 1 : ", solution_m1(1) , end="\n\n")
    # print("method 2 : ", solution_m2(arr) , end="\n\n")



