class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        max_h = 0
        max_h_indices = []
        for i in range(len(heights)):
            index = len(heights)-1-i
            h = heights[index]
            if h > max_h:
                max_h = h
                max_h_indices.append(index)

        return max_h_indices[::-1]