class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row or rows exceed string length
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row = 0
        step = 1

        # Traverse each character and place in correct row
        for c in s:
            rows[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        # Combine all rows
        return ''.join(rows)


# Example
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
