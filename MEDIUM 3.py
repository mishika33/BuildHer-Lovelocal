class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # Check if the matrix is empty or None
        if matrix is None or len(matrix) < 1:
            return 0

        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize a 2D array for dynamic programming
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0

        # Iterate through each cell in the matrix
        for r in range(rows):
            for c in range(cols):
                # If the cell contains '1', update dp and calculate the maximum side length
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r+1][c+1])

        # Calculate and return the area of the maximal square
        return max_side * max_side


# Example usage with the given input
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Given input matrix
    input_matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    # Call the maximalSquare method and print the result
    result = solution.maximalSquare(input_matrix)
    print(result)
    
