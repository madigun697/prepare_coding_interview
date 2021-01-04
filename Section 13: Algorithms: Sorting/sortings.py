print('Bubble Sort')
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(bubbleSort(numbers))

print('Selection Sort')
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(arr):
	for i in range(len(arr)):
		minIdx = i
		for j in range(i+1, len(arr)):
			if arr[minIdx] > arr[j]:
				minIdx = j
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	return arr

print(selectionSort(numbers))

print('Insertion Sort')
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(arr):
	for i in range(1, len(arr)):
		for j in range(i):
			if arr[j] > arr[i]:
				arr.insert(j, arr[i])
				del arr[i+1]
				break
	
	return arr

print(insertionSort(numbers))

print('Merge Sort')
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(arr):
	if len(arr) == 1:
		return arr

	leftArr = arr[:len(arr) // 2]
	rightArr = arr[len(arr) // 2:]

	return mergeArrs(mergeSort(leftArr), mergeSort(rightArr))

def mergeArrs(arr1, arr2):
	i = 0
	j = 0
	sortedArr = []

	while True:
		if i == len(arr1):
			sortedArr += arr2[j:]
			break
		if j == len(arr2):
			sortedArr += arr1[i:]
			break

		if arr1[i] <= arr2[j]:
			sortedArr.append(arr1[i])
			i += 1
		else:
			sortedArr.append(arr2[j])
			j += 1

	return sortedArr

print(mergeSort(numbers))

print('Quick Sort')
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quickSort(arr):
	if len(arr) < 2:
		return arr

	partitionIdx = 0
	pivotIdx = 1
	for i in range(1, len(arr)):
		if arr[i] < arr[partitionIdx]:
			arr[pivotIdx], arr[i] = arr[i], arr[pivotIdx]
			pivotIdx += 1

	arr[partitionIdx], arr[pivotIdx-1] = arr[pivotIdx-1], arr[partitionIdx]

	if len(arr) == 2:
		return arr

	return quickSort(arr[:pivotIdx-1]) + [arr[pivotIdx-1]] + quickSort(arr[pivotIdx:])

print(quickSort(numbers))
