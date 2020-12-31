# Merge Two Arrays and Sort

def mergeSortedArrays(arr1, arr2):
	assert len(arr1) > 0 or len(arr2) > 0, 'Check your inputs'

	arr = arr2 if len(arr1) == 0 else arr1 if len(arr2) == 0 else arr1 + arr2
	# if len(arr1) == 0:
	# 	arr = arr2
	# elif len(arr2) == 0:
	# 	arr = arr1
	# else:
	# 	arr = arr1 + arr2

	arr = sorted(arr)

	print(arr)

# If these two arrays are already sorted
def mergeSortedArrays2(arr1, arr2):
	assert len(arr1) > 0 or len(arr2) > 0, 'Check your inputs'

	totalLength = len(arr1) + len(arr2)
	arr = []
	i = j = 0

	for l in range(totalLength-1):
		if arr1[i] > arr2[j]:
			arr.append(arr2[j])
			j += 1
		else:
			arr.append(arr1[i])
			i += 1

	if i == len(arr1)-1:
		arr.append(arr1[i])
	else:
		arr.append(arr2[j])
	
	print(arr)

mergeSortedArrays([0,3,4,31], [4,6,30])
mergeSortedArrays2([0,3,4,31], [4,6,30])