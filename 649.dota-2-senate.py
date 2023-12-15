#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        ban_r = ban_d = 0

        # As long as Operation 2 is not possible, True
        while 'R' in senate and 'D' in senate:

            # Create a new stack of survivors for potential next round
            game = deque()

            for i, k in enumerate(senate) :

                # If senate is pending ban, don't include to next round
                if k == 'R' and ban_r == 0:
                    ban_d += 1
                    game.append(k)
                elif k == 'R' and ban_r > 0 :
                    ban_r -= 1
                elif k == 'D' and ban_d == 0 :
                    ban_r += 1
                    game.append(k)
                elif k == 'D' and ban_d > 0 :
                    ban_d -= 1
            
            # Update senate for next round
            senate = ''.join(game)
            
        return "Radiant" if 'R' in senate else "Dire"
    
# @lc code=end

