# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop.

def findFactorialRecursive(number):
	if number == 1:
		return 1

	return number * findFactorialRecursive(number-1)

def findFactorialIterative(number):
	answer = 1
	for i in range(number, 1, -1):
		answer *= i
	return answer

print(findFactorialRecursive(5))
print(findFactorialIterative(5))