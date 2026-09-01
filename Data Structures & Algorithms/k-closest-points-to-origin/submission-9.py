import heapq
import math
from collections import deque
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist_sq = -(x**2 + y**2)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist_sq, [x, y]))
            else:
                if dist_sq > max_heap[0][0]:
                    heapq.heappushpop(max_heap, (dist_sq, [x, y]))

        return [point for (dist, point) in max_heap]