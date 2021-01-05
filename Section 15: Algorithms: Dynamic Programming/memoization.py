print('No Memoization')
def addTo80(n):
	print('long time')
	return n + 80

print(addTo80(5))
print(addTo80(5))
print(addTo80(5))

print()
print('Memoization')
cache = {}
def memoizedAddTo80(n):
	if cache.get(n) != None:
		return cache.get(n)
	else:
		print('long time')
		cache[n] = n + 80
		return cache.get(n)

print(memoizedAddTo80(5))
print(memoizedAddTo80(5))
print(memoizedAddTo80(5))

print()
print('Memoization2')

def memoizedAddTo80():
	cache = {}
	def addTo80(n):
		if cache.get(n) != None:
			return cache.get(n)
		else:
			print('long time')
			cache[n] = n + 80
			return cache.get(n)

	return lambda x: addTo80(x)

memoized = memoizedAddTo80()
print(memoized(5))
print(memoized(5))
print(memoized(5))