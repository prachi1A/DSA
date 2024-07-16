'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            if cnt == 0:
                cnt += 1
                el = i
            elif i == el:
                cnt += 1
            else:
                cnt -= 1
        
        if nums.count(el)>(len(nums)/2):
            return el
        else:
            return -1

    '''
    O(N^2) Brute force

    '''
    #     class Solution:
    # def majorityElement(self, A, N):
        
    #     dic = {item : A.count(item) for item in A}
        
    #     for k,v in dic.items():
    #         if v > N//2:
    #             return k
    #         else:
    #             return -1

        