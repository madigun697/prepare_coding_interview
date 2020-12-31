class LinkedList:
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
		self.head = LinkedListNode(value)
		self.tail = self.head

	# O(1)
	def append(self, value):
		if self.head == None:
			self.initializeList(value)
		else:
			self.tail.next = LinkedListNode(value)
			self.tail = self.tail.next

		self.length += 1

	# O(1)
	def prepend(self, value):
		if self.head == None:
			self.initializeList(value)
		else:
			self.head = LinkedListNode(value, self.head)

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
			lookupNode = self.lookup(index-1)
			newNode = LinkedListNode(value, lookupNode.next)
			lookupNode.next = newNode

			self.length += 1

	# O(n)
	def remove(self, index):
		assert index >= 0 and index < self.length

		if index == 0:
			self.head = self.head.next
		elif index == self.length-1:
			lookupNode = self.lookup(index-1)
			lookupNode.next = None
			self.tail = lookupNode
		else:
			lookupNode = self.lookup(index-1)
			lookupNode.next = self.lookup(index+1)
		
		self.length -= 1

	def reverse(self):
		# if self.length < 2:
		# 	return

		# values = []

		# currentNode = self.head
		# for _ in range(self.length):
		# 	values.append(currentNode.value)
		# 	currentNode = currentNode.next
		
		# self.head = LinkedListNode(values[-1])
		# self.tail = self.head
		# for i in range(-2, -(self.length+1), -1):
		# 	self.tail.next = LinkedListNode(values[i])
		# 	self.tail = self.tail.next


		if self.length < 2:
			return

		firstNode = self.head
		secondNode = self.head.next
		while secondNode != None:
			remainNodes = secondNode.next
			secondNode.next = firstNode
			firstNode = secondNode
			secondNode = remainNodes

		self.tail = self.head
		self.tail.next = None
		self.head = firstNode

class LinkedListNode:
	def __init__(self, value, next=None):
		self.value = value
		self.next = None

		if next != None:
			self.next = next		
	
	def __str__(self):
		return '{ value: %d, next: %s }' % (self.value, self.next)