# https://leetcode.com/problems/flood-fill/submissions/
# Resouorce: https://www.youtube.com/watch?v=TClRuEZ-uDg&t=211s
class Solution:
    def floodFill(self, image: List[List[int]], i: int, j: int, newColor: int) -> List[List[int]]:
        if not image or len(image) == 0 or image[i][j] == newColor:
            return image
        return self.fill(image, i, j, image[i][j], newColor)
    
    def fill(self, image, i, j, color, newColor):
        if j > len(image[0])-1 or j < 0 or i > len(image)-1 or i < 0 or color != image[i][j]:
            return image
        image[i][j] = newColor
        image = self.fill(image, i, j+1, color, newColor)
        image = self.fill(image, i, j-1, color, newColor)
        image = self.fill(image, i+1, j, color, newColor)
        image = self.fill(image, i-1, j, color, newColor)
        return image