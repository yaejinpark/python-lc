# A tree is a recursive data structure where a child node is another tree in itself.
# Real benefit of a tree structure is the speed.

class Tree:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self,child):
		child.parent = self # A child node is an instance of a Tree class.
		self.children.append(child)

	def get_level(self): # Telling you the level of nodes
		level = 0 
		p = self.parent

		while p:
			level += 1
			p = p.parent

		return level

	def print_tree(self):
		spaces = self.get_level() * ' ' * 3 # Put in three spaces per level in front of node
		prefix = spaces + "|__" if self.parent else"" # Put in '|__' for all nodes except the root node

		print(prefix + self.data)

		if len(self.children) > 0:
			for child in self.children:
				child.print_tree()

# Example: building a tree for electronics
def build_product_tree():
	# Level 0
	root = Tree('Electronics')

	# Level 1
	laptop = Tree('Laptop')
	smartphone = Tree('Smartphone')
	root.add_child(laptop)
	root.add_child(smartphone)

	# Level 2
	smartphone.add_child(Tree('iPhone'))
	smartphone.add_child(Tree('Galaxy'))
	laptop.add_child(Tree('Macbook'))
	laptop.add_child(Tree('Surface'))

	return root

electronics = build_product_tree()
electronics.print_tree()