'''
Find the contiguous subarray within an array, A of length N which has the largest sum.
Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.

Average time :- 33 min
Time Taken :- 12 min
'''

def maxSubArray(A):
    # take a variable for tracking the max sum
    # and other for tracking local sum which can set to 0 if 
    # it went down to 0 
    max_sum = A[0]
    max_local = 0
    for i in range(len(A)):
        max_local += A[i]
        # updating max sum if a greater sum found
        max_sum = max(max_local, max_sum)
        if max_local < 0:
            max_local = 0
    return max_sum

print(maxSubArray([-1,-2,-3]))