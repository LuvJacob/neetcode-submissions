class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in board:
            nums_found = set()
            for j in i:
                if j == ".":
                    continue
                elif j in nums_found:
                    return False
                else:
                    nums_found.add(j)
        for x in range(9):      # columns
            nums_found_col = set()
            for i in board:
                
                if i[x] == ".":
                    continue
                elif i[x] in nums_found_col:
                    return False
                else:
                    nums_found_col.add(i[x])
        for r in range(0,9,3):
            for c in range(0,9,3):
                found = set()
                for i in range(3):
                        for j in range(3):
                            if board[r+i][c+j] == ".":
                                continue
                            elif board[r+i][c+j] in found:
                                return False
                            else:
                                found.add(board[r+i][c+j])
        return True
                   
                    

                
        