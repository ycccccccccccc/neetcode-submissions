class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        t, b = 0, len(matrix) - 1
        
        if target < matrix[-1][0]:
            while t <= b:
                m = (t+b)//2
                print(t, b, m)
                if target < matrix[m][0]:
                    b = m - 1
                elif target >= matrix[m][0] and target < matrix[m+1][0]:
                    row = m
                    break
                else:
                    t = m + 1
        else:
            row = b
        print(row)
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False