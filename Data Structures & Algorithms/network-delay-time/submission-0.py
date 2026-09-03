import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue = [(0, k)]
        edges = defaultdict(list)
        visited = set()
        duration = 0

        for source, target, time in times:
            edges[source].append((target, time))

        while queue:
            curr_time, curr_node = heapq.heappop(queue)

            if curr_node in visited:
                continue
            
            duration = curr_time
            visited.add(curr_node)
            
            for target, time in edges[curr_node]:
                if target not in visited:
                    heapq.heappush(queue, (curr_time + time, target))

        return duration if len(visited) == n else -1
            
