# https://leetcode.com/problems/validate-binary-search-tree/submissions/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isValidBST(self, root):
		self.minValue = (-2 ** 31) - 1
		self.result = True
		self.getMinValue(root)
        
		return self.result
        
	def getMinValue(self, currentNode):
		if not self.result:
			return
        
		if currentNode.left != None:
			self.getMinValue(currentNode.left)
        
		if self.minValue < currentNode.val:
			self.minValue = currentNode.val
		else:
			self.result = False
			return
            
		if currentNode.right != None:
			self.getMinValue(currentNode.right)