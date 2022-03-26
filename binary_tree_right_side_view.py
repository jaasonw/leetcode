# https://leetcode.com/problems/binary-tree-right-side-view/submissions/

class Solution(object):
    # This is the solution I came up with on the spot for my Amazon interview,
    # ngl I had no clue how to do a BFS so I did this with a DFS instead as 
    # well as recursively
    def rightSideView_dfs(self, root):
        if root == None: return []
        line_of_sight = {}
        stack = []
        stack.append((root, 0))
        while len(stack) > 0:
            node, level = stack.pop()
            line_of_sight[level] = node.val
            if node.right != None:
                stack.append((node.right, level+1))
            if node.left != None:
                stack.append((node.left, level+1))
        return list(line_of_sight.values())
    # This is the more correct way to do it, with a BFS, which coincidentally
    # looks identical to the code for my DFS implementation
    def rightSideView(self, root):
        if root == None: return []
        queue = deque()
        line_of_sight = {}
        queue.append((root, 0))
        while len(queue) > 0:
            node, level = queue.popleft()
            line_of_sight[level] = node.val
            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))
        return list(line_of_sight.values())
