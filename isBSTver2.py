"""	Version 1 above runs slowly since it traverses over some parts of the tree many times. A better solution looks at each
node only once. The trick is to write a utility helper function isBSTRecur(struct node* node, int min, int max) that
traverses down the tree keeping track of the narrowing min and max allowed values as it goes, looking at each node
only once. The initial values for min and max should be INT_MIN and INT_MAX -- they narrow from there.	"""


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

	def _isBST(self,minm,maxm):
		if self.data < minm or self.data > maxm:
			return False
		left = right = True
		if self.left:
			left = self.left._isBST(minm,self.data)
		if self.right:
			right = self.right._isBST(self.data+1,maxm)
		return left and right


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

	def isBST(self,INT_MIN,INT_MAX):
		if self.root == None:
			return True

		return self.root._isBST(INT_MIN,INT_MAX)


r = BinaryTree()
r.insert(5)
r.root.left = TreeNode(2)
r.root.right = TreeNode(7)
r.root.left.left =  TreeNode(1)
r.root.left.right =  TreeNode(6)


r.printTree()
print r.isBST(0,5)
