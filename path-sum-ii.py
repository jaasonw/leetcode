# https://leetcode.com/problems/path-sum-ii/submissions/

class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return []
        stack = [(root, [root.val], root.val)]
        paths = []
        while stack:
            current_node, current_nums, current_sum = stack.pop()
            if current_sum == targetSum and not current_node.right and not current_node.left:
                paths.append(current_nums)
                continue
            if current_node.right:
                stack.append(
                    (
                        current_node.right,
                        [*current_nums, current_node.right.val],
                        current_node.right.val + current_sum
                    )
                )

            if current_node.left:
                stack.append(
                    (
                        current_node.left,
                        [*current_nums, current_node.left.val],
                        current_node.left.val + current_sum
                    )
                )
        return paths
