class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


n = 5
linkls = LinkedList()
for i in range(n):
    linkls.append(i)
    # print(i)

sum = 0
last = linkls.head
while last.next:
    sum += last.data
    last = last.next
sum += last.data
print(sum)