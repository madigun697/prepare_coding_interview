class MyArray:
	def __init__(self):
		self.length = 0
		self.data = {}

	def __str__(self):
		return '{ length: %d, data: %s }' % (self.length, self.data)

	def get(self, index):
		return self.data[index]
	
	def push(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def pop(self):
		lastItem = self.data[self.length-1]
		del self.data[self.length-1]
		self.length -= 1
		return lastItem

	def delete(self, index):
		deleteItem = self.data[index]
		self.shiftItems(index)
		return deleteItem

	def shiftItems(self, index):
		for i in range(index, self.length-1):
			self.data[i] = self.data[i+1]
		del self.data[self.length-1]
		self.length -= 1


newArray = MyArray()
newArray.push('hi')
print(newArray)

newArray.push('you')
print(newArray)

newArray.push('!')
print(newArray.pop())
print(newArray)

newArray.push('!')
newArray.push('are')
newArray.push('nice')
print(newArray)

print(newArray.delete(2))
print(newArray)
