from collections import deque

queue = deque()

print(queue)

queue.append(1)
queue.append(2)

print(queue)

queue.appendleft(5)
queue.append(7)
print(queue)

queue.pop()
queue.popleft()
print(queue)