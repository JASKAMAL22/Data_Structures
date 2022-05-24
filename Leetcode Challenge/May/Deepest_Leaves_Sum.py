'''
STATEMENT:
Given the root of a binary tree, return the sum of values of its deepest leaves.
--------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        q = deque()
        q.append(root)
        q.append(None)
        s = 0
        while q:
            node = q.popleft()
            if node == None:
                if not q:
                    return s
                s = 0
                q.append(None)
                continue
            s += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
'''
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
-----------------
Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

'''
