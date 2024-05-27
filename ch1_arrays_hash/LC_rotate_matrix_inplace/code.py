# %%
from typing import List

class Solution:

    def get_xy_from_ij(self, i, j, len_matrix):
        if len_matrix % 2 == 0:
            # len(matrix) = 4, i=0,x=-2, i=3,x=2
            if i > half:
                y = (i-half+1)*-1
            else:
                y = (i-half)*-1

            if j > half:
                x = j-half+1
            else:
                x = j-half

        else:
            half = int(len_matrix/2)
            y=(i-half)*-1            
            x=j-half

        return x, y

    def get_ij_from_xy(self, x, y, len_matrix):
        if len_matrix % 2 == 0:
            
        else:
            if x == 0:
                j = int(len_matrix / 2)
            elif x > 0:
                    
            

    

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = matrix.copy()

        self.create_xy_from_ij(matrix)
        self.create_ij_from_xy()

        for i in range(len(matrix)):
            for j in range(len(matrix)):

                old_y, old_x = self.get_xy_from_ij(i,j)

                new_x = 0*old_x + 1*old_y 
                new_y = -1*old_x + 0*old_y
                                
                new_j, new_i = self.get_ij_from_xy(new_x, new_y)

                matrix[new_i][new_j] = matrix_copy[i][j] 

# %%
matrix=[[1,2,3],[4,5,6],[7,8,9]]

s = Solution()
# %%
s.rotate(matrix)
s.coordinates
s.coordinates_rev
# %%
