# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder :
#             return None
#         rootval = preorder[0]
#         root = TreeNode(rootval)
#         mid = inorder.index(rootval)

#         root.left = self.buildTree (
#             preorder[1:mid+1],
#             inorder[:mid]
#         )

#         root.right = self.buildTree(
#             preorder[mid+1:],
#             inorder[mid+1:]
#         )

#         return root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {value: i for i, value in enumerate(inorder)}
        pre_index = 0

        def build(left, right):

            nonlocal pre_index

            if left > right:
                return None

            root_val = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)