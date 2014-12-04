"""	Change a tree so that the roles of the left and right pointers are swapped at every node.	"""


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

	def swapLeftRight(self):
		self.left,self.right = self.right,self.left
		if self.left:
			self.left.swapLeftRight()
		if self.right:
			self.right.swapLeftRight()


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

	def mirror(self):
		if self.root:
			self.root.swapLeftRight()
		else:
			print '\tempty tree'



t = BinaryTree()
t.insert(2)
t.insert(1)
t.insert(3)

print 'tree t :'
t.printTree()

t.mirror()

print 'after mirroring '
t.printTree()
