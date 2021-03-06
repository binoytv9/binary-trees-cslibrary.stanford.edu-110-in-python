"""	Write an isBST() function that returns true if a tree is a binary search tree
and false otherwise. Suppose you have helper functions minValue() and maxValue() that return the min or max int value from a
non-empty tree	"""


class TreeNode:
	def __init__(self,data,left=None,right=None,parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def has_left_child(self):
		return self.left

	def has_right_child(self):
		return self.right

	def _printTree(self):
		if self != None:
			if self.has_left_child():
				self.left._printTree()
			print self.data,' ',
			if self.has_right_child():
				self.right._printTree()

	def _isBST(self):
		if self.left and self.left.minValue() > self.data:
			return False
		if self.right and self.right.maxValue() <= self.data:
			return False
		if (self.left and not self.left._isBST()) or (self.right and not self.right._isBST()):
			return False
		return True

	def minValue(self):
		if self == None:
			print '\ttree empty'
			return
		current = self
		while current.left != None:
			current = current.left
		return current.data

	def maxValue(self):
		if self == None:
			print '\ttree empty'
			return
		current = self
		while current.right != None:
			current = current.right
		return current.data


class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			self._put(data, self.root)
		else:
			self.root = TreeNode(data)

	def _put(self, data, current_node):
		if data < current_node.data:
			if current_node.has_left_child():
				self._put(data, current_node.left)
			else:
				current_node.left = TreeNode(data, parent = current_node)
		else:
			if current_node.has_right_child():
				self._put(data, current_node.right)
			else:
				current_node.right = TreeNode(data, parent = current_node)

	def printTree(self):
		if self.root:
			self.root._printTree()
			print '\n\n'
		else:
			print '\ttree empty'

	def isBST(self):
		if self.root == None:
			return True

		return self.root._isBST()


r = BinaryTree()
r.insert(5)
r.root.left = TreeNode(2)
r.root.right = TreeNode(7)
r.root.left.left =  TreeNode(1)
r.root.left.right =  TreeNode(6)


r.printTree()
print r.isBST()
