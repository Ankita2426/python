import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap,value)
    return [heapq.heappop(heap) for i in range(len(heap))]
print(heapsort([12,3,5,6,0,1]))
