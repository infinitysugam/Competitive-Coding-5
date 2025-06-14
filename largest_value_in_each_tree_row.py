# Time Complexity = O(n)
# Space Complexity = O(n)
import collections


class Solution:
    def largestValues(self,root):
        if not root:
            return []

        queue = collections.deque()
        result = []

        level = 0 

        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(0,size):
                element = queue.popleft()
                if i == 0 and element:
                    result.append(element.val)
                else:
                    if element and result[level]<element.val:
                        result[level]=element.val
                
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            level = level + 1
        return result



        
