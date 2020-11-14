class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        TC : O(m * n)
        SC : O(m * n)
        m --> # rows
        n --> cols
        """
        if image[sr][sc] == newColor:
            return image
        self.dfs(sr, sc, image[sr][sc], newColor, image)
        return image

    def dfs(self, i, j, color, newColor, image):
        if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != color:
            return
        image[i][j] = newColor
        self.dfs(i - 1, j, color, newColor, image)
        self.dfs(i + 1, j, color, newColor, image)
        self.dfs(i, j - 1, color, newColor, image)
        self.dfs(i, j + 1, color, newColor, image)
