class Solution:
    # Dynamic Programming
    # Time: O(n*sqrt(n)), Space: O(n)
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(int(sqrt(i))):
                dp[i] = min(dp[i], dp[i-(j+1)**2] + 1)
        return dp[-1]

    # # BFS
    # # Maybe.... Time: O(n), Space: O(n)
    # # because we don't revisit those same valued nodes, 
    # # therefore, at most we visit all the node from value 0 to value n, 
    # # it is O(n) in the worst case; in practice, 
    # # bfs tends to stop early, so on average it should be better than O(n); 
    # # not sure if there is a good way to get an even tighter bounds

    # def numSquares(self, n: int) -> int:
    #     # Initialize the queue for BFS
    #     queue = deque([(n, 0)])  # Each entry is (remaining sum, steps taken)
    #     visited = set()  # To avoid revisiting the same state

    #     while queue:
    #         remaining, steps = queue.popleft()
            
    #         # Check all perfect squares less than or equal to remaining
    #         for i in range(1, int(remaining**0.5) + 1):
    #             square = i * i
    #             next_remaining = remaining - square
                
    #             if next_remaining == 0:  # Found the solution
    #                 return steps + 1
                
    #             if next_remaining not in visited:  # Add to queue if not visited
    #                 visited.add(next_remaining)
    #                 queue.append((next_remaining, steps + 1))
        
    #     return -1  # Should not reach here


##
# class Solution:
#     def numSquares(self, n):
        
#         def is_divided_by(n, count):
#             """
#                 return: true if "n" can be decomposed into "count" number of perfect square numbers.
#                 e.g. n=12, count=3:  true.
#                      n=12, count=2:  false
#             """
#             if count == 1:
#                 return n in square_nums
            
#             for k in square_nums:
#                 if is_divided_by(n - k, count - 1):
#                     return True
#             return False

#         square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
#         for count in range(1, n+1):
#             if is_divided_by(n, count):
#                 return count
