#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        diff = [[0] * m for i in range(n)]

        ones_row = [row.count(1) for row in grid]
        ones_col = [col.count(1) for col in zip(*grid)]

        for i in range(n) :
            for j in range(m) :
                diff[i][j] = ones_row[i] + ones_col[j] - (m - ones_row[i]) - (n - ones_col[j])

        return diff

        # # [row] : (row)
        # cache = defaultdict(lambda:0)
        # diff = [[0] * len(grid[0]) for i in range(len(grid))]
        # #print(diff)

        # for i in range(len(grid)) :

        #     key = tuple(grid[i])
        #     #if key not in cache :

        #     balance = 0
        #     for j in range(len(key)) :

        #         if grid[i][j] == 0 :
        #             balance -= 1
        #             cache[j] -= 1
        #         else :
        #             balance += 1
        #             cache[j] += 1

        #     cache[key] = balance

        # #print(cache)

        # for i in range(len(diff)) :
        #     key = tuple(grid[i])
        #     for j in range(len(key)) :
        #         #print(cache[key], cache[j])
        #         diff[i][j] = cache[key] + cache[j]

        # #print(diff)

        # return diff
    
# @lc code=end

