'''
STATEMENT:
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
----------------------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return False
            if node == target: return True
            L, R = dfs(node.left), dfs(node.right)
            if L or R: self.path += [0] if L else [1]
            return L or R
        
        self.path = []
        dfs(original)
        for i in self.path[::-1]:
            cloned = cloned.left if i == 0 else cloned.right
        
        return cloned
'''
TEST CASE 1:-
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. 
The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
-------------------------------------------
TEST CASE2:-
Input: tree = [7], target =  7
Output: 7
'''
'''

