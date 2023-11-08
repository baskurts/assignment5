class Node:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt

# Step 1: Create the linked list
head = Node(1, Node('+', Node(1, Node('=', Node(2)))))
print(head)
# Step 2: Create a second reference, named operator, to the linked list of nodes.
operator = head.next.next  # This points to the node with value '1' that comes after '+'.

# Step 3: Change the operator reference
operator.value = '='

# Step 4: Create a third reference, named result, to the linked list of nodes.
result = operator.next.next  # This points to the node with value '2'.

# Step 5: Change the result reference
result.value = None

# Steps 6-15: More changes will be applied following similar logic.

# Step 16: We'll write the code to display information about copies of the list later.

# Function to print the list for verification purposes
def print_list(node):
    while node:
        print(node.value, end=' -> ' if node.next else '\n')
        node = node.next

# Verify the current list structure
print_list(head)
