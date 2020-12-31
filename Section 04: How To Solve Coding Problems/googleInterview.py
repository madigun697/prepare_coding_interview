# Problem
# Given a array and a integer, whether there is a pair in the array that their sum is the same to given integer or not.

# Sample
# [1,2,4,9], 8 - False
# [1,2,4,4], 8 - True
# [6,4,3,2,1,7], 9 - True

# Brute-force solution
def isPairWithSum1(arr, target):
	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			if arr[i] + arr[j] == target:
				return True
	return False
# Time Complexity: O(n^2)
# Space Complexity: O(1)
print('--- Brute-Force ---')
print(isPairWithSum1([1,2,4,9], 8))
print(isPairWithSum1([1,2,4,4], 8))
print(isPairWithSum1([6,4,3,2,1,7], 9))

def isPairWithSum2(arr, target):
	i = 0
	j = len(arr)-1
	while i < j:
		subsum = arr[i] + arr[j]
		if subsum == target:
			return True
		elif subsum > target:
			j -= 1
		elif subsum < target:
			i += 1
	return False
# Time Complexity: O(n)
# Space Complexity: O(1)
# However, this function only works under the condition that the given array is sorted
print('--- Solution 2 ---')
print(isPairWithSum2([1,2,4,9], 8))
print(isPairWithSum2([1,2,4,4], 8))
print(isPairWithSum2([6,4,3,2,1,7], 9))

def isPairWithSum3(arr, target):
	needNums = {}
	for num in arr:
		if needNums.get(num):
			return True
		else:
			needNums[target-num] = True
	return False
# Time Complexity: O(n)
# Space Complexity: O(n)
print('--- Solution 3 ---')
print(isPairWithSum3([1,2,4,9], 8))
print(isPairWithSum3([1,2,4,4], 8))
print(isPairWithSum3([6,4,3,2,1,7], 9))
print('-------------------')