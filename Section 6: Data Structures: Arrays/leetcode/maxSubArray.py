# https://leetcode.com/problems/maximum-subarray/description/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# TestCase
# [-2,1,-3,4,-1,2,1,-5,4] => 6
# [-2,-2,-2,-3,-4,1] => 1

# Alone:		-2	1	-3	4	-1	2	1		-5	4
# SubSum:		-2	-2	-2	2	3	5	6		1	5
# compare:		=	>	<	>	<	<	<		<	<
# Switch:		x	o	x	o	x	x	x		x	x
# FinSubSum:	-2	1	-2	4	3	5	6(max)	1	5

# Alone:		-2	-2	-2	-3	-4	1
# SubSum:		-2	-4	-4	-7	-7	-3
# compare:		=	>	>	>	>	>
# Switch:		x	o	o	o	o	o
# FinSubSum:	-2	-2	-2	-3	-4	1(max)

def maxSubArray(nums):
	assert type(nums) == list
	assert len(nums) >= 1

	if len(nums) == 1:
		return nums[0]

	maxSum = -2 ** 31 # Minimum possible value
	subSum = 0

	for num in nums:
		subSum += num

		if subSum < num:
			subSum = num
		
		maxSum = max(maxSum, subSum)
	
	return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-2,-2,-2,-3,-4,1]))