class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = board[:][:]
        cols = [[board[i][j] for i in range(9)] for j in range(9)]
        boxes = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                boxes[(i//3) * 3 + j//3].append(board[i][j])

        def is_uniq(arr: List[str]):
            arr_strp = [x for x in arr if x != '.']
            return len(arr_strp) == len(set(arr_strp))
        
        ok_col = all(map(is_uniq, cols))
        ok_row = all(map(is_uniq, rows))
        ok_box = all(map(is_uniq, boxes))
        return ok_box and ok_col and ok_row
