class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        i = 0
        while i < len(asteroids):
            asteroid = asteroids[i]
            if (stack and (asteroid < 0 and stack[-1] > 0)):
                if (abs(asteroid) > abs(stack[-1])):
                    stack.pop()
                elif (abs(asteroid) == abs(stack[-1])):
                    stack.pop()
                    i += 1
                else:
                    i += 1
            else:
                stack.append(asteroid)
                i += 1

        return stack
