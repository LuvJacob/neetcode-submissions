class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0

        for low in range(0,len(heights)):
            for high in range (low+1, len(heights)):
                height = min(heights[low],heights[high])
                width = high - low
                area = width * height
                most = max(area, most)
        return most
            
        