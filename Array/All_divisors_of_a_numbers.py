'''
Given an integer N, print all the divisors of N in the ascending order.
 

Example 1:

Input : 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely 
divisible by 1, 2, 4, 5, 10 and 20.

Example 2:

Input: 21191
Output: 1 21191
Explanation: As 21191 is a prime number,
it has only 2 factors(1 and the number itself).

Your Task:

Your task is to complete the function print_divisors() which takes N as input parameter and prints all the factors of N as space seperated integers in sorted order. You don't have to print any new line after printing the desired output. It will be handled in driver code.
 

Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(sqrt(N))
 

Constraints:
1 <= N <= 105
'''

class Solution:
    def print_divisors(self, N):
        # code here
        divisors = []
        # if N ==1:
        #     print(1)
        
        # else:
        for i in range(1, int(N**0.5) + 1):
                if N % i == 0:
                    divisors.append(i)
                    if i != N / i:
                        divisors.append(N // i)
                        
            # Sort the divisors once before printing
        for i in range(len(divisors)): 
          print(sorted(divisors)[i], end=" ")
              
#             
# class Solution:
#     def print_divisors(self, N):
#         # code here
#         divisors = []
#         for i in range(1, int(N**0.5)+1):
#           if N % i == 0:
#              divisors.append(i)
#              if i!=N/i:
#                 divisors.append(N//i)
#         for i in range(len(divisors)): 
#           print(sorted(divisors)[i], end=" ")

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends