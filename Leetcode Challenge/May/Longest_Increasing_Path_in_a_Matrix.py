'''
STATEMENT:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
----------------------------------------------------------------
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Step 1: build a directed acyclic graph
	    graph = collections.defaultdict(list)
	    indegree = collections.defaultdict(int)
	    for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
			    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
			    for x, y in neighbors:
				    if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[i][j] < matrix[x][y]:
					    graph[(i,j)].append((x,y))
					    indegree[(x,y)]+=1

	    # Step 2: Topological sorting with Kahn's algorithm
	    queue = collections.deque([(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if (i,j) not in indegree])
	    max_path_len = 0
	    while queue:
		    max_path_len += 1
		    for _ in range(len(queue)):
			    node = queue.popleft()
			    for neigh in graph[node]:
				    indegree[neigh] -= 1
				    if not indegree[neigh]:
					    queue.append(neigh)
	    return max_path_len

'''
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
'''
