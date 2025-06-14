# Time complexity = O(m*n)
# Space Complexity = O(m*n)
class Solution:
    def isValidSudoku(self, board) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))