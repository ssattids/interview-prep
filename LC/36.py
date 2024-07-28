class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_array(array):
            check_array = []
            for item in array:
                if item != ".":
                    check_array.append(item)
            num_set = set({'1','2','3','4','5','6','7','8','9'})
            check_set = set(check_array)
            #make sure the numbers are in the 1,2...9 range
            if (check_set - num_set) != set():
                return False
            if len(check_set) != len(check_array):
                return False
            return True 

        # check row
        for row in board:
            if check_array(row) == False:
                return False
        # check column
        for i in range(len(board[0])):
            col_array = []
            for row in board:
                col_array.append(row[i])
            if check_array(col_array) == False:
                return False
            
        # check small individual squares
        for i in range(0,9,3):
            row_group = board[i:i+3]
            for j in range(3):
                values = []
                for row in row_group:
                    values += row[j*3:(j+1)*3]
                if check_array(values) == False:
                    return False

        return True

