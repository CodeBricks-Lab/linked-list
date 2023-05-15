
class Node():
    def __init__(self, value):
        print('called init function')
        self.value = value
        self.next = None
    
    def __str__(self):
        return f'{self.value}'

    def next_node(self, node):
        self.next = node

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

# n1.next = n2
# n2.next = n3
n1.next_node(n2)
n2.next_node(n3)
# n1 -> n2 -> n3
current_node = n1

while True:
    print(current_node)
    current_node = current_node.next






