'''
You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.

Example 1:

Input: 200
Output: 2
Explanation: By reversing the digits of 
number, number will change into 2.
Example 2:

Input : 122
Output: 221
Explanation: By reversing the digits of 
number, number will change into 221.


Your Task:
You don't need to read or print anything. Your task is to complete the function reverse_digit() which takes N as input parameter and returns the reversed number.
 

Expected Time Complexity: O(Log(N))
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 1015
'''
class Solution:
	def reverse_digit(self, n):
		rev_num = 0
		while n>0:
		     last_digit = n%10
			 n = n//10
		     rev_num = rev_num*10 + last_digit
		return rev_num

