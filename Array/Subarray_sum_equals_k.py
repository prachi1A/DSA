'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #optimal
        prefix_sum = 0
        no_of_subar = 0
        h = {0:1} #hashtable
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in h:
                no_of_subar += h[prefix_sum-k]
            if prefix_sum not in h:
                h[prefix_sum] = 1
            else:
                h[prefix_sum] += 1
        return no_of_subar

        # cnt = 0   O(N^2)
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i, len(nums)):
        #         s += nums[j]
        #         if s == k:
        #             cnt += 1
        # return cnt
      


        # cnt = 0  O(N^3)
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i+1,len(nums)+1):
        #         s = sum(nums[i:j])
        #         if s == k:
        #             cnt+=1
        #         s = 0
        # return cnt
            
