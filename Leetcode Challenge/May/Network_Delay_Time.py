'''
STATEMENTS:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

-----------------------------------------------------------------------
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, k)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == n else -1
      
'''
Test Cases:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
---------------------------
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
'''
