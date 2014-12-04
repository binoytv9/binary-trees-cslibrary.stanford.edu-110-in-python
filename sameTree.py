"""	Given two binary trees, return true if they are structurally identical -- they are made of nodes with the same values
arranged in the same way.	"""


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

	def sameNode(self,other):
		if self.left and self.right and other.left and other.right:
			return self.data == other.data and self.left.sameNode(other.left) and self.right.sameNode(other.right)
		elif self.left or self.right or other.left or other.right:
			return False
		else:
			return self.data == other.data


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
				
	def sameTree(self,other):
		if self.root == None and other.root == None:
			return True
		elif self.root == None or other.root == None:
			return False
		else:
			return self.root.sameNode(other.root)
		



t = BinaryTree()
t.insert(2)
t.insert(1)
t.insert(3)

r = BinaryTree()
r.insert(2)
r.insert(4)
r.insert(3)

print 'tree t :'
t.printTree()
print 'tree r :'
r.printTree()

print t.sameTree(r)
