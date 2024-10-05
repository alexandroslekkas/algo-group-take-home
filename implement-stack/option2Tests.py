from option2 import IntStack, IntStackNode

# Initialize stack
root = IntStackNode(0)
stack = IntStack(root)

# Push some elements onto the stack
stack.push(IntStackNode(1))
stack.push(IntStackNode(2))
stack.push(IntStackNode(3))
stack.push(IntStackNode(4))
stack.push(IntStackNode(5))

# Test if the size and last elements are correct
assert stack.size() = 6
assert stack.peek() = 5

# Remove an item
stack.pop()

# Perform the same check again to see if popping worked
assert stack.size() = 5
assert stack.peek() = 4

# Push the value we popped before back again
stack.push(IntStackNode(6))

# Check to see if we pushed correctly
assert stack.size() = 6
assert stack.peek() = 5

