class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        seen_col , seen_row = set() , set()
        for i in range(0 , n ):
            for j in range(0, n ):
                if board[i][j] != ".":
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])
            seen_col , seen_row = set() , set()
        for x in range(0 , n  , 3 ):
            for y in range(0 , n  , 3 ):
                seen_box = set()
                for c in range(x , x + 3 ):
                    for r in range(y , y + 3 ):
                        if board[c][r] == ".":
                            continue
                        if board[c][r] in  seen_box:
                            return False
                        seen_box.add(board[c][r])
        return True