# https://leetcode.com/problems/rotate-array/description/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:
#     Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?

# TestCase
# [1,2,3,4,5,6,7], 3 => [5,6,7,1,2,3,4]
# [-1,-100,3,99], 2 => [3,99,-1,-100]

class Solution:	
	def setNums(self, nums):
		assert type(nums) == list
		assert len(nums) >= 1
		self.nums = nums

	def rotate(self, nums, k):
		assert type(k) == int
		assert k >= 0
		self.setNums(nums)

		if k == 0: return

		l = len(nums)
        tempNums = nums[:l-k]
        
        del nums[:l-k]
        nums += tempNums

	def rotate2(self, nums, k):
		assert type(k) == int
		assert k >= 0
		self.setNums(nums)

		if k == 0: return

		l = k & len(self.nums)
		self.nums = self.nums[-l:] + self.nums[:-l]


solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)
print(solution.nums)
solution.rotate([-1,-100,3,99], 2)
print(solution.nums)