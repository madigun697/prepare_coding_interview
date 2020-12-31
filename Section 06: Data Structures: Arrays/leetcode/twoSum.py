# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Test Case
# [2,7,11,15], 9 => (0,1)
# [3,2,4], 6 => (1,2)
# [3,3], 6 => (0,1)

# `nums` is not sorted
# Elements of `nums` are not unique

# O(n^2)
def twoSum(nums, target):
	assert type(nums) == list
	assert type(target) == int
	assert len(nums) >= 2

	for i in range(len(nums)-1):
		for j in range(1, len(nums)):
			if nums[i] + nums[j] == target:
				return (i, j)

# O(n)
def twoSum(nums, target):
	assert type(nums) == list
	assert type(target) == int
	assert len(nums) >= 2

	availableNums = {}

	for i in range(len(nums)):
		if availableNums.get(nums[i]) != None:
			return (availableNums.get(nums[i]), i)
		else:
			availableNums[target - nums[i]] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))