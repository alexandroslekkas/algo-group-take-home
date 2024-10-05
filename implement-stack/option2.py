# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class IntStack:
    def __init__(self, root):
        self.root = root
        
    def push(self, node):
        currentNode = self.root
        while (currentNode.getNext() != 0):
            currentNode = currentNode.getNext()
        currentNode.setNext(node)
        
    def pop(self):
        previousNode = 0
        currentNode = self.root
        while (currentNode.getNext() != 0):
            previousNode = currentNode
            currentNode = currentNode.getNext()
        previousNode.setNext(0)
        
    def peek(self):
        currentNode = self.root
        while (currentNode.getNext() != 0):
            currentNode = currentNode.getNext()
        return currentNode.getValue()     
    
    def size(self):
        count = 1
        currentNode = self.root
        while (currentNode.getNext() != 0):
            currentNode = currentNode.getNext()
            count = count + 1
        return count
    
class IntStackNode:
    next = 0
    
    def __init__(self, value):
        self.value = value
        
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def getValue(self):
        return self.value





        
    
        
