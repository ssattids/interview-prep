"""
https://leetcode.com/problems/pascals-triangle-ii/?envType=daily-question&envId=2023-10-16
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        ith_1_pascal_triangle = [1,1]
        for index in range(2, rowIndex+1):
            ith_pascal_triangle = []
            ith_pascal_triangle.append(1)
            j = 0
            while(j+1 != len(ith_1_pascal_triangle)):
                ith_pascal_triangle.append(ith_1_pascal_triangle[j] + ith_1_pascal_triangle[j+1])
                j+=1
            ith_pascal_triangle.append(1)

            ith_1_pascal_triangle = ith_pascal_triangle

        return ith_1_pascal_triangle


