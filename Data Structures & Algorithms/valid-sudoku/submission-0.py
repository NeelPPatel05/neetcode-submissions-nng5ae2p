class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = {}
        row_map = {}
        block_map = {}

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n != ".":
                    col_set = col_map.setdefault(j, set())
                    row_set = row_map.setdefault(i, set())
                    block_set = block_map.setdefault((i//3, j//3), set())

                    if n in col_set: return False
                    col_set.add(n)

                    if n in row_set: return False
                    row_set.add(n)

                    if n in block_set: return False
                    block_set.add(n)

        return True
