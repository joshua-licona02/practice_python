import heapq

minHeap = []

heapq.heappush(minHeap,3)
heapq.heappush(minHeap,4)
heapq.heappush(minHeap,2)

print(minHeap[0])
print(minHeap)

while len(minHeap):
    print(heapq.heappop(minHeap))

print(minHeap)

maxHeap=[]

heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap,-2)

print(-1* maxHeap[0])
print(maxHeap)

while len(maxHeap):
    print(heapq.heappop(maxHeap))


# Build heap from initial values
    arr = [2,1,8,4,5]
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))