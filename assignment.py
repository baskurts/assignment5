class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creating nodes
node1 = Node(1)
plus_node = Node('+')
equal_node = Node('=')
node2 = Node(2)
none_node = Node(None)

# Linking nodes
head = node1
node1.next = plus_node
plus_node.next = equal_node
equal_node.next = node2
node2.next = none_node

# 2
operator = plus_node

# 3
operator = equal_node

# 4
result = node2

# 5
result = none_node

# 6
result.data = 0

# 7
plus_node.data = '*'

result.data = 1

# 8




