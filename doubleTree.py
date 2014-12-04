"""	For each node in a binary search tree, create a new duplicate node, and insert the duplicate as the left child of the
original node. The resulting tree should still be a binary search tree.	"""


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

	def _doubleTree(node):
		if node != None:
			if node.has_left_child():
				node.left._doubleTree()
			if node.has_right_child():
				node.right._doubleTree()

			node.left = TreeNode(node.data,node.left)


class BinaryTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def insert(self, data):
		if self.root:
			self._put(data, self.root)
		else:
			self.root = TreeNode(data)
			self.size = self.size + 1

	def _put(self, data, current_node):
		if data < current_node.data:
			if current_node.has_left_child():
				self._put(data, current_node.left)
			else:
				current_node.left = TreeNode(data, parent = current_node)
		else:
			if current_node.has_right_child():
				self._put(data, current_node.right_child)
			else:
				current_node.right = TreeNode(data, parent = current_node)

	def printTree(self):
		if self.root:
			self.root._printTree()
			print
		else:
			print 'tree empty'
				
	def doubleTree(self):
		if self.root:
			self.root._doubleTree()
		else:
			print 'tree empty'



t = BinaryTree()
t.insert(2)
t.insert(1)
t.insert(3)

t.printTree()
t.doubleTree()
t.printTree()
