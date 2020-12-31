class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def __str__(self):
		return '{\n\thead: %s, \n\ttail: %s, \n\tlength: %d\n}' % (self.head, self.tail, self.length)

	# O(n)
	def printList(self):
		valueList = []
		node = self.head
		while node != None:
			valueList.append(node.value)
			node = node.next
		print(valueList)

	# O(1)
	def initializeList(self, value):
		self.head = DoublyLinkedListNode(value)
		self.tail = self.head

	# O(1)
	def append(self, value):
		if self.head == None:
			self.initializeList(value)
		else:
			self.tail.next = DoublyLinkedListNode(value, prev=self.tail)
			self.tail = self.tail.next

		self.length += 1

	# O(1)
	def prepend(self, value):
		if self.head == None:
			self.initializeList(value)
		else:
			newNode = DoublyLinkedListNode(value, next=self.head)
			self.head.prev = newNode
			self.head = newNode

		self.length += 1

	# O(n)
	def lookup(self, index):
		assert index >= 0 and index < self.length

		if index == 0:
			return self.head
		elif index == self.length-1:
			return self.tail
		else:
			lookupNode = self.head
			for i in range(index):
				lookupNode = lookupNode.next
			return lookupNode

	# O(n)
	def insert(self, index, value):
		if index <= 0:
			self.prepend(value)
		elif index >= self.length:
			self.append(value)
		else:
			prevNode = self.lookup(index-1)
			nextNode = self.lookup(index)
			newNode = DoublyLinkedListNode(value, prev=prevNode, next=nextNode)
			prevNode.next = newNode
			nextNode.prev = newNode

			self.length += 1

	# O(n)
	def remove(self, index):
		assert index >= 0 and index < self.length

		if index == 0:
			self.head = self.head.next
			self.head.prev = None
		elif index == self.length-1:
			lookupNode = self.lookup(index-1)
			lookupNode.next = None
			self.tail = lookupNode
		else:
			prevNode = self.lookup(index-1)
			nextNode = self.lookup(index+1)
			prevNode.next = nextNode
			nextNode.prev = prevNode
		
		self.length -= 1

class DoublyLinkedListNode:
	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.prev = None
		self.next = None

		if prev != None:
			self.prev = prev

		if next != None:
			self.next = next
	
	def __str__(self):
		return '{ value: %d, prev: %s, next: %s }' % (self.value, str(self.prev.value) if self.prev != None else 'None', self.next)

myLinkedList = DoublyLinkedList()
myLinkedList.printList()

myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.printList()

myLinkedList.append(16)
myLinkedList.printList()

myLinkedList.prepend(4)
myLinkedList.prepend(18)
myLinkedList.printList()

myLinkedList.insert(2, 7)
myLinkedList.insert(4, 99)
myLinkedList.printList()

print(myLinkedList.lookup(4))

myLinkedList.remove(4)
myLinkedList.remove(0)
myLinkedList.remove(4)
myLinkedList.printList()

print(myLinkedList)