#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS,COLS=len(matrix)-1,len(matrix[0])-1
        res=0
        for r in range(ROWS,-1,-1):
            for c in range(COLS,-1,-1):
                if r>=ROWS or c>=COLS: #for right and bottom boundary 
                    down=right=diag=0
                else:
                    down=int(matrix[r][c+1])
                    right=int(matrix[r+1][c])
                    diag=int(matrix[r+1][c+1])

                if matrix[r][c]=="1":
                    matrix[r][c]=1+(min(down,right,diag))
                    res=max(res,matrix[r][c])   

        return res*res

        # if len(matrix) + len(matrix[0]) == 2 : return int(matrix[0][0])
        # # Djikstras with 2D DP

        # m = len(matrix[0])
        # n = len(matrix)
        # largestSquare = [0]

        # cache = {}    # (i, j) : largest so far

        # def dfs(i, j) :
        #     if i >= n or j >= m :
        #         return 0
        #     #print(i, j, matrix[i][j] is 0, matrix[i][j])
        #     if (i, j) in cache :
        #         return cache[(i, j)]

        #     # Gets unique longest values of neighbors
        #     #neighbors = list(dict.fromkeys([dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1)]).keys())

        #     neighbors = [dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1)]
        #     if matrix[i][j] == "0" :
        #         return 0

        #     howManyZeroes = neighbors.count(0)

        #     unique = set(neighbors)
        #     unique.discard(1)
        #     # print(unique)
        #     if (len(set(neighbors)) - len(unique) == 1) and howManyZeroes == 0:
        #         print("doubled")
        #         # neighbors[2] == diagonal
        #         # Simple formula for next sqrted size
        #         largestSquare[0] = max(largestSquare[0], int(pow(sqrt(neighbors[2]) + 1, 2)))
        #         cache[(i, j)] = int(pow(sqrt(neighbors[2]) + 1, 2))
        #     else :
        #         largestSquare[0] = max(largestSquare[0], 1)
        #         cache[(i, j)] = 1
        #     #print(set(neighbors))
        #     print(i, j, neighbors, matrix[i][j], largestSquare[0])

        #     # if (howManyZeroes == 0 or isSqr(totalOnes)) and largestSquare[0] < totalOnes :
        #     #     largestSquare[0] = totalOnes
        #     #print(totalOnes)

        #     return cache[(i, j)]

        # def isSqr(i) :
        #     return i == math.isqrt(i) ** 2
        
        # dfs(0, 0)
        # #print(cache)
        # #print(largestSquare[0])
        # return largestSquare[0]


# @lc code=end

