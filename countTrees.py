"""	Suppose you are building an N node binary search tree with the values 1..N. How many structurally different
binary search trees are there that store those values	"""


def countTrees(numKeys):
	if numKeys <= 1:
		return 1
	else:
		_sum = 0
		root = 1
		while root <= numKeys:
			left = countTrees(root-1)
			right = countTrees(numKeys-root)
			_sum += left*right
			root += 1

		return _sum


print countTrees(4)
