# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:

#     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

class MyStack:
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

# Solution 1
# Push: O(n), Pop: O(1)
# class MyQueue:
# 	def __init__(self):
# 		"""
# 		Initialize your data structure here.
# 		"""
# 		self.stack = MyStack()

# 	def __str__(self):
# 		return ','.join([str(e) for e in self.stack.data])

# 	def push(self, x: int) -> None:
# 		"""
# 		Push element x to the back of queue.
# 		"""
# 		tempStack = MyStack()
# 		for _ in range(len(self.stack.data)):
# 			tempStack.push(self.stack.pop())
# 		self.stack.push(x)
# 		for _ in range(len(tempStack.data)):
# 			self.stack.push(tempStack.pop())

# 	def pop(self) -> int:
# 		"""
# 		Removes the element from in front of queue and returns that element.
# 		"""
# 		return self.stack.pop()

# 	def peek(self) -> int:
# 		"""
# 		Get the front element.
# 		"""
# 		return self.stack.peek()

# 	def empty(self) -> bool:
# 		"""
# 		Returns whether the queue is empty.
# 		"""
# 		return self.stack.isEmpty()
        
# Solution 2
# Push: O(1), Pop: Amortized O(1)
class MyQueue:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.stack1 = MyStack()
		self.stack2 = MyStack()
		self.top = None

	def __str__(self):
		return ','.join([str(e) for e in self.stack2.data + self.stack1.data])

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		if self.stack1.isEmpty():
			self.top = x

		self.stack1.push(x)

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		if self.stack2.isEmpty():
			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())

		return self.stack2.pop()

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		if self.stack2.isEmpty():
			return self.top
		else:
			return self.stack2.peek()

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		return self.stack1.isEmpty() and self.stack2.isEmpty()


# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
print(myQueue)
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue)
print(myQueue.peek()) # return 1
print(myQueue)
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue)
print(myQueue.empty()) # return false