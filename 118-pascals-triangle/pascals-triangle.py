class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []
        
        # iterate over the number of rows
        for i in range(numRows):
            # create anew row filled with 1s
            row = [1] * (i+1)

            # update elements in the midlle based on previous row
            for j in range(1,i):
                row[j] = res[i-1][j-1] + res[i-1][j]

            # Append the cro
            res.append(row)

        return res
        