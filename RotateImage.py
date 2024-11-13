class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #vertical reflection

        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n - j - 1] = matrix[i][n - j - 1],matrix[i][j]
        
