# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n):
	cache = {1:1, 2:2}
        
	def climb(n):
		if cache.get(n) == None:
			cache[n] = climb(n-1) + climb(n-2)
		return cache[n]
	
	return climb(n)

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(5))
# 1: 1+1+1+2
# 2: 2+1+2
# 3: 1+2+2
# 4: 1+1+2+1
# 5: 2+2+1
# 6: 1+1+1+1+1
# 7: 2+1+1+1
# 8: 1+2+1+1