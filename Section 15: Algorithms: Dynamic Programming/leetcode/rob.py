# https://leetcode.com/problems/house-robber/
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

def rob1(nums):
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return max(nums[0], nums[1])
			
	cache = {}
	def robbing(house):
		if house >= len(nums):
			return 0

		if cache.get(house) == None:
			cache[house] = nums[house] + max(robbing(house + 2), robbing(house + 3))
		return cache[house]

	return max(robbing(0), robbing(1))

def rob2(nums):
	dp = [0] * len(nums)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])
	for i in range(2, len(nums)):
		dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
	
	return dp[-1]

nums = [1,2,3,1]
print(rob1(nums))
print(rob2(nums))

nums = [2,1,1,2]
print(rob1(nums))
print(rob2(nums))

nums = [2,3,2]
print(rob1(nums))
print(rob2(nums))