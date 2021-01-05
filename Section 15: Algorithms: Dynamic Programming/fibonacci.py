calculation = 0
def fibonacci(n):
	global calculation
	calculation += 1
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(10))
print(calculation)
print('----')

calculation = 0
def fibonacciDP():
	cache = {0: 0, 1: 1}
	def fib(n):
		global calculation
		calculation += 1
		if cache.get(n) == None:
			cache[n] = fib(n-2) + fib(n-1)
		return cache.get(n)
	return lambda x: fib(x)

fib = fibonacciDP()
print(fib(10))
print(calculation)