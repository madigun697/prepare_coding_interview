# https://leetcode.com/problems/move-zeroes/description/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# TestCase
# [0,1,0,3,12] => [1,3,12,0,0]

class Solution:
	def __init__(self, nums):
		assert type(nums) == list
		self.nums = nums

	def moveZeros(self):
		if len(self.nums) <= 1:
			return

		removeIndex = []
		for i in range(len(self.nums)-1, -1, -1):
			if self.nums[i] == 0:
				removeIndex.append(i)
		
		for i in removeIndex:
			del self.nums[i]
			self.nums.append(0)

	def moveZeros2(self):
		if len(self.nums) <= 1:
			return

		zeroIndex = 0
		for i in range(len(self.nums)):
			if self.nums[i] != 0:
				self.nums[zeroIndex], self.nums[i] = self.nums[i], self.nums[zeroIndex]
				zeroIndex += 1


solution = Solution([0,1,0,3,12])
solution.moveZeros2()
print(solution.nums)