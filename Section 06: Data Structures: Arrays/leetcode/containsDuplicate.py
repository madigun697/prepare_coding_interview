# https://leetcode.com/problems/contains-duplicate/description/
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# TestCase
# [1,2,3,1] => true
# [1,2,3,4] => false
# [1,1,1,3,3,4,3,2,4,2] => true

def containsDuplicate(nums):
	assert type(nums) == list
	assert len(nums) > 0

	if len(nums) == 1:
		return False

	mapping = {}
        
	for num in nums:
		if mapping.get(num):
			return True
		else:
			mapping[num] = True
			
	return False

def containsDuplicate2(nums):
	assert type(nums) == list
	assert len(nums) > 0

	return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print('----')
print(containsDuplicate2([1,2,3,1]))
print(containsDuplicate2([1,2,3,4]))
print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))