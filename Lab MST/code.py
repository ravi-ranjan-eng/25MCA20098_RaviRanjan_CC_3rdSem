# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def generate(start,end):
            if start>end:
                return [None]
            result=[]
            for i in range(start,end+1):
                leftTrees=generate(start,i-1)
                rightTrees=generate(i+1,end)
                for left in leftTrees:
                    for right in rightTrees:
                        rootNode=TreeNode(i)
                        rootNode.left=left
                        rootNode.right=right
                        result.append(rootNode)
            return result
        return generate(1,n)
             
