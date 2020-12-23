# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# should return true.

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']

array3 = ['a', 'b', 'c', 'x']
array4 = ['z', 'y', 'x']

def getCommonItem1(arr1, arr2):
	# Brute force code
	for item1 in arr1:
		for item2 in arr2:
			if item1 == item2:
				return True
	
	return False
# Time complexity is O(a*b)
# Space complexity is O(1)
print(getCommonItem1(array1, array2))
print(getCommonItem1(array3, array4))

def getCommonItem2(arr1, arr2):
	# Create dictionary with first array
	firstArray = dict.fromkeys(arr1, True)
	for item in arr2:
		# If the dictionary which based on first array has key that is same to item of seconde array, these two arrays have common item
		if firstArray.get(item):
			return True
	
	return False
# Time complexity is O(a+b)
# Space somplextiy is O(a), because we assign the new dictionary with first array's size
print(getCommonItem2(array1, array2))
print(getCommonItem2(array3, array4))