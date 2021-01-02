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

tree = BinarySearchTree()
# tree.insert(9)
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)

# tree.print()

# print(tree.lookup(20))
# print(tree.lookup(99))

# for v in [60, 30, 72, 14, 51, 1, 38, 52, 44, 56, 54, 55, 58]:
# 	tree.insert(v)

# tree.print()
# tree.remove(52)
# tree.remove(51)
# print()
# tree.print()
# tree.remove(102134123)

for v in [10,5,15,1,8,11,18]:
	tree.insert(v)

tree.print()
tree.remove(10)
print()
tree.print()