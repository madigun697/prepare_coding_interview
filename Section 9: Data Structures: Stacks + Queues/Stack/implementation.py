from LinkedList import LinkedList

class Stack:
	def __init__(self):
		self.data = LinkedList()

	def push(self, value):
		self.data.append(value)

	def pop(self):
		if self.isEmpty():
			return None
		item = self.data.tail.value
		self.data.remove(self.data.length-1)
		return item

	def peek(self):
		if self.isEmpty():
			return None
		return self.data.tail.value

	def isEmpty(self):
		return self.data.length == 0

myStack = Stack()
print(myStack.isEmpty())

myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.push('youtube')
myStack.data.printList()
print(myStack.isEmpty())

print(myStack.pop())
myStack.data.printList()
print(myStack.pop())
myStack.data.printList()

print(myStack.peek())
myStack.data.printList()
print(myStack.pop())
myStack.data.printList()
print(myStack.pop())
myStack.data.printList()

print('----')

class ArrayStack:
	def __init__(self):
		self.data = []

	def push(self, value):
		self.data.append(value)

	def pop(self):
		assert len(self.data) > 0
		item = self.data[-1]
		self.data = self.data[:-1]
		return item

	def peek(self):
		assert len(self.data) > 0
		return self.data[-1]

	def isEmpty(self):
		return len(self.data) == 0

myStack = ArrayStack()
print(myStack.isEmpty())

myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.push('youtube')
print(myStack.data)
print(myStack.isEmpty())

print(myStack.pop())
print(myStack.data)
print(myStack.pop())
print(myStack.data)

print(myStack.peek())
print(myStack.data)
print(myStack.pop())
print(myStack.data)
print(myStack.pop())
print(myStack.data)