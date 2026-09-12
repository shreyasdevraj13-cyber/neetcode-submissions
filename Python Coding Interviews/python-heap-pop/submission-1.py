import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    heapq.heapify(heap)
    res = []
    while len(heap) != 0:
        res.append(heapq.heappop(heap))
    return res


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([12, 10, 9, 8, 7, 6]))
