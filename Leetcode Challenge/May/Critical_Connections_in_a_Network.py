'''
STATEMENT:
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.
--------------------------------------------------------------------------
Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
---------------------------------------------------------------------
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)] ## vertex i ==> [its neighbors]
		
        currentRank = 0 ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
		
        lowestRank = [i for i in range(n)] ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
		
        visited = [False for _ in range(n)] ## common DFS/BFS method to mark whether this node is seen before
        
        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        res = []
        prevVertex = -1 ## This -1 a dummy. Does not really matter in the beginning. 
		## It will be used in the following DFS because we need to know where the current DFS level comes from. 
		## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
		
        currentVertex = 0 ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        visited[currentVertex] = True 
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
				# We avoid visiting visited nodes here instead of doing it at the beginning of DFS - 
				# the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex]) 
			# take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1: ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])
'''
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
'''
