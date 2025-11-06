from collections import deque

# Create an empty queue using deque (double-ended queue)
# deque is a data structure from the 'collections' module that allows fast appends and pops
# from both the left and right sides — ideal for implementing queues and stacks efficiently.
queue = deque([])

# Add elements to the right side of the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Remove elements from the left side of the queue (FIFO behavior)
queue.popleft()
queue.popleft()
queue.popleft()

# Check if the queue is empty
if not queue:
    print("empty")

# Print the current state of the queue (should be empty)
print(queue)
