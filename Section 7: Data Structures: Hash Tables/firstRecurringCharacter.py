# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return None

# def firstRecurringCharacter(arr):
# 	minIndex = len(arr)
# 	for i in range(len(arr)-1):
# 		if i == minIndex:
# 			return arr[minIndex]
# 		for j in range(i+1, len(arr)):
# 			if arr[i] == arr[j]:
# 				if minIndex > j:
# 					minIndex = j
	
# 	return None

def firstRecurringCharacter(arr):
	appearMap = {}

	for v in arr:
		if appearMap.get(v):
			return v
		else:
			appearMap[v] = True
	
	return None

print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,3,4,5]))