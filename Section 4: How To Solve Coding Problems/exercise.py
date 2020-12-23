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
	for item1 in arr1:
		for item2 in arr2:
			if item1 == item2:
				return True
	
	return False

print(getCommonItem1(array1, array2))
print(getCommonItem1(array3, array4))

def getCommonItem2(arr1, arr2):
	firstArray = dict.fromkeys(arr1, True)
	for item in arr2:
		if firstArray.get(item):
			return True
	
	return False

print(getCommonItem2(array1, array2))
print(getCommonItem2(array3, array4))