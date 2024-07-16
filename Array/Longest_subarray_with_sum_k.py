'''
Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

 

Examples:
 

Input :
arr[] = {10, 5, 2, 7, 1, 9}, k = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
Input : 
arr[] = {-1, 2, 3}, k = 6
Output : 0
Explanation: 
There is no such sub-array with sum 6.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

 

Constraints:
1<=n<=105
-105<=arr[i], K<=105
'''

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        max_len = 0
        prefix_sum = 0
        h = {}
        for i in range(n):
            prefix_sum += arr[i]
           
            if prefix_sum == k:
                max_len = max(max_len, i+1)
                
            if (prefix_sum - k) in h:
                max_len = max(max_len, i-h[prefix_sum-k])
                
            if prefix_sum not in h: #to store the prefix sum and it's index
                h[prefix_sum] = i #why this loop not operated at the first: because you might store prefix_sum prematurely, missing the opportunity to correctly update max_len when conditions require it.

                
        return max_len