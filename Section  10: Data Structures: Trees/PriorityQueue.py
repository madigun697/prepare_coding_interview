class QElement:
	def __init__(self, value, priority):
		self.value = value
		self.priority = priority

	def __str__(self):
		return 'Value: %d, Prioirty: %d' % (self.value, self.priority)

class PriorityQueue:
	def __init__(self):
		self.data = []

	def enqueue(self, value, priority):
		qElement = QElement(value, priority)

		for idx, element in enumerate(self.data):
			if element.priority > priority:
				self.data.insert(idx, qElement)
				return

		self.data.append(qElement)

	def dequeue(self):
		if self.isEmpty():
			return
		
		self.data = self.data[1:]

	def front(self):
		if self.isEmpty():
			return

		return self.data[0]

	def rear(self):
		if self.isEmpty():
			return

		return self.data[-1]

	def isEmpty(self):
		return len(self.data) == 0

	def print(self):
		for element in self.data:
			print(element)

pQueue = PriorityQueue()
pQueue.print()

pQueue.enqueue(123, 2)
pQueue.enqueue(3, 3)
pQueue.enqueue(34, 2)
pQueue.enqueue(14, 1)
pQueue.enqueue(5, 5)
pQueue.enqueue(734, 8)
pQueue.print()
print('----')
pQueue.dequeue()
pQueue.print()
print('----')
print(pQueue.front())
print(pQueue.rear())