class HashTable:
	def __init__(self, size):
		self.data = [None] * size
		self.size = size
		self.keyList = []

	def _hash(self, key):
		hash = 0
		for i in range(len(key)):
			hash = (hash + ord(key[i]) * i) % self.size

		return hash

	def set(self, key, value):
		index = self._hash(key)
		if self.data[index] == None:
			self.data[index] = []

		self.data[index].append((key, value))
		self.keyList.append(key)

	def get(self, key):
		index = self._hash(key)
		if self.data[index] != None:
			for k, value in self.data[index]:
				if k == key:
					return value
		else:
			return None

	def keys(self):
		# keys = []
		# for data in self.data:
		# 	if data != None and len(data) > 0:
		# 		for key, _ in data:
		# 			keys.append(key)

		# return keys
		return self.keyList

myHashTable = HashTable(50)
print(myHashTable._hash('grapes'))

myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))

myHashTable.set('AI', 99999)
print(myHashTable.get('grapes'))
print(myHashTable.get('AI'))

print(myHashTable.get('apples'))

print(myHashTable.keys())