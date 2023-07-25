class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # if len(stack) == 0 or stack[-1] < 0:
                #     stack.append(a)
                # else:
                while len(stack) > 0 and stack[-1] > 0 and -a > stack[-1]:
                    stack.pop()
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(a)
                if len(stack) > 0 and stack[-1] > 0 and -a == stack[-1]:
                    stack.pop()
   
        return stack
