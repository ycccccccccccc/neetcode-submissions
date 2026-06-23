class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False]*9 for i in range(9)]
        cols = [[False]*9 for i in range(9)]
        boxes = [[False]*9 for i in range(9)]

        for y in range(9):
            for x in range(9):
                num_str = board[y][x]
                if num_str != '.':
                    num = int(num_str) - 1
                    if rows[y][num]:
                        return False
                    if cols[x][num]:
                        return False
                    if boxes[x//3+(y//3)*3][num]:
                        return False

                    rows[y][num] = True
                    cols[x][num] = True
                    boxes[x//3+(y//3)*3][num] = True

        return True

