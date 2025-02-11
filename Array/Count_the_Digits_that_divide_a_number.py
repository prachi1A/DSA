'''Problem statement:
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
'''
class Solution:
    def countDigits(self, num: int) -> int:
       cnt = 0
       org_num = num
       while org_num>0:
         digit = org_num%10
         org_num = org_num//10
         if digit!=0 and num%digit == 0:
            cnt+=1
       return cnt
    