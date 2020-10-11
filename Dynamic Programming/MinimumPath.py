def minimize_path(grid):
    """
    https://leetcode.com/problems/minimum-path-sum/
    TC : O(m * n)
    SC : O(1)
    Dynamic Programming Approach
    :param grid:
    :return: total cost to reach from topLeft to bottomRight
    """
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    for row in range(m):
        for col in range(n):
            if row == 0 and col != 0:
                grid[row][col] += grid[row][col - 1]
            elif row != 0 and col == 0:
                grid[row][col] += grid[row - 1][col]
            elif row != 0 and col != 0:
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[m-1][n-1]

if __name__ == "__main__":
    grid = [[1,1,3],
            [2,3,1],
            [4,6,1]
            ]
    assert (minimize_path(grid) == 7)