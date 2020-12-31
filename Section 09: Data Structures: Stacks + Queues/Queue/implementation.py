from LinkedList import LinkedList

class Queue:
	def __init__(self):
		self.data = LinkedList()

	def peek(self):
		if self.isEmpty():
			return None
		
		return self.data.head.value

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		if self.isEmpty():
			return None

		item = self.data.head.value
		self.data.remove(0)
		return item

	def isEmpty(self):
		return self.data.length == 0

myQueue = Queue()
print(myQueue.isEmpty())

myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')
myQueue.data.printList()
print(myQueue.isEmpty())

print(myQueue.dequeue())
myQueue.data.printList()
print(myQueue.dequeue())
myQueue.data.printList()

print(myQueue.peek())
myQueue.data.printList()
print(myQueue.dequeue())
myQueue.data.printList()
print(myQueue.dequeue())
myQueue.data.printList()