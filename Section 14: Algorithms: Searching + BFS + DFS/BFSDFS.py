class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def __str__(self):
		return 'Node value: %d, Left node: %s, Right node: %s' % (self.value, self.left.value if self.left != None else 'None', self.right.value if self.right != None else 'None')

	def isLeaf(self):
		return self.left == None and self.right == None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def print(self):
		currentNodes = [self.root]
		level = 1
		nodes = {}
		nodes[level] = [n for n in currentNodes]
		while len(currentNodes) > 0:
			level += 1
			nodes[level] = []
			nextNodes = []
			for node in currentNodes:
				if node.left != None:
					nodes.get(level).append(node.left)
				if node.right != None:
					nodes.get(level).append(node.right)		
				nextNodes += [node.left, node.right]

			currentNodes = [n for n in nextNodes if n != None]
		if len(nodes.get(level)) == 0:
			del nodes[level]

		for k, v in nodes.items():
			print('level %d' % k)
			for n in v:
				print(n)

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			newNode = Node(value)
			parentNode = self.root
			while True:
				if parentNode.value > value:
					if parentNode.left == None:
						parentNode.left = newNode
						break
					else:
						parentNode = parentNode.left
				elif parentNode.value < value:
					if parentNode.right == None:
						parentNode.right = newNode
						break
					else:
						parentNode = parentNode.right
				else:
					print('Existed value')
					return

	def lookup(self, value):
		if self.root == None:
			return None

		currentNode = self.root
		while currentNode != None:
			if currentNode.value == value:
				return currentNode

			if currentNode.value > value:
				currentNode = currentNode.left
			else:
				currentNode = currentNode.right
		
		return None

	def remove(self, value):
		assert self.root != None

		parentNode = None
		directionFlag = ''
		currentNode = self.root

		while currentNode != None:
			if currentNode.value > value:
				directionFlag = 'left'
				parentNode = currentNode
				currentNode = currentNode.left
			elif currentNode.value < value:
				directionFlag = 'right'
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				if currentNode.isLeaf():
					if directionFlag == 'left':
						parentNode.left = None
					elif directionFlag == 'right':
						parentNode.right = None
				elif currentNode.left == None:
					if directionFlag == 'left':
						parentNode.left = currentNode.right
					elif directionFlag == 'right':
						parentNode.right = currentNode.right
				elif currentNode.right == None:
					if directionFlag == 'left':
						parentNode.left = currentNode.left
					elif directionFlag == 'right':
						parentNode.right = currentNode.left
				else:
					replaceNode = currentNode.right
					while replaceNode.left != None:
						if replaceNode.left.left == None:
							tempNode = replaceNode.left
							replaceNode.left = tempNode.right
							replaceNode = tempNode
						else:
							replaceNode = replaceNode.left
					replaceNode.left = currentNode.left
					replaceNode.right = currentNode.right

					if directionFlag == 'left':
						parentNode.left = replaceNode
					elif directionFlag == 'right':
						parentNode.right = replaceNode
					else:
						self.root = replaceNode
				break

	def breadthFirstSearch(self):
		currentNode = self.root
		nodeList = []
		nodeQueue = []
		nodeQueue.append(currentNode)

		while len(nodeQueue) > 0:
			currentNode = nodeQueue[0]
			nodeQueue = nodeQueue[1:]
			nodeList.append(currentNode.value)
			if currentNode.left != None:
				nodeQueue.append(currentNode.left)
			if currentNode.right != None:
				nodeQueue.append(currentNode.right)

		return nodeList

	def BFS(self):
		return self.breadthFirstSearchRecursive([], [self.root])

	def breadthFirstSearchRecursive(self, nodeList, queue):
		if len(queue) == 0:
			return nodeList

		currentNode = queue[0]
		queue = queue[1:]

		nodeList.append(currentNode.value)
		if currentNode.left != None:
			queue.append(currentNode.left)
		if currentNode.right != None:
			queue.append(currentNode.right)
		
		return self.breadthFirstSearchRecursive(nodeList, queue)

	def DFS(self, orderType):
		if orderType == 'InOrder':
			return self.depthFirstSearchInOrder(self.root, [])
		elif orderType == 'PreOrder':
			return self.depthFirstSearchPreOrder(self.root, [])
		elif orderType == 'PostOrder':
			return self.depthFirstSearchPostOrder(self.root, [])

	def depthFirstSearchInOrder(self, currentNode, nodeList):
		if currentNode.left != None:
			nodeList = self.depthFirstSearchInOrder(currentNode.left, nodeList)
		nodeList.append(currentNode.value)
		if currentNode.right != None:
			nodeList = self.depthFirstSearchInOrder(currentNode.right, nodeList)

		return nodeList

	def depthFirstSearchPreOrder(self, currentNode, nodeList):
		nodeList.append(currentNode.value)
		if currentNode.left != None:
			nodeList = self.depthFirstSearchPreOrder(currentNode.left, nodeList)
		if currentNode.right != None:
			nodeList = self.depthFirstSearchPreOrder(currentNode.right, nodeList)

		return nodeList

	def depthFirstSearchPostOrder(self, currentNode, nodeList):
		if currentNode.left != None:
			nodeList = self.depthFirstSearchPostOrder(currentNode.left, nodeList)
		if currentNode.right != None:
			nodeList = self.depthFirstSearchPostOrder(currentNode.right, nodeList)

		nodeList.append(currentNode.value)
		return nodeList



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

#     9
#  4     20
#1  6  15  170

print('Breadth First Search')
print(tree.breadthFirstSearch())
print(tree.BFS())

print()
print('Depth First Search')
print('''InOrder
[1, 4, 6, 9, 15, 20, 170]
InOrder return the sorted list

PreOrder
[9, 4, 1, 6, 20, 15, 170]
PreOrder list is useful recreation of tree

PostOrder
[1, 6, 4, 15, 170, 20, 9]
''')
print(tree.DFS('InOrder'))
print(tree.DFS('PreOrder'))
print(tree.DFS('PostOrder'))