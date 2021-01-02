# Givne a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 -> 2+3

# O(n)
def fibonacciIterative(n):
	if n <= 1:
		return n
	else:
		a = 0
		b = 1
		for i in range(n-1):
			a, b = b, a+b
		return b

# O(2^n)
def fibonacciRecursive(n):
	if n <= 1:
		return n
	else:
		return fibonacciRecursive(n-2) + fibonacciRecursive(n-1)

print(fibonacciIterative(5))
print(fibonacciRecursive(5))
print('----')
print(fibonacciIterative(8))
print(fibonacciRecursive(8))