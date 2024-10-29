class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Step 1: Create an adjacency list and a visited array
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # Array to hold the course order
        result = []
        # To detect a cycle
        visiting = set()
        visited = set()
        
        # Step 2: Define a DFS function
        def dfs(course):
            # If the course is being visited, a cycle exists
            if course in visiting:
                return False
            # If the course has already been visited, skip it
            if course in visited:
                return True
            
            # Mark the course as being visited
            visiting.add(course)
            
            # Visit all prerequisite courses
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            
            # Mark the course as visited
            visiting.remove(course)
            visited.add(course)
            # Add the course to the result as it has no more prerequisites
            result.append(course)
            
            return True
        
        # Step 3: Perform DFS for each course
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []  # Return an empty array if a cycle is detected
        
        # Return the courses in the order to take them
        return result  
        
        # h = {i: [] for i in range(numCourses)}
        # for q, p in prerequisites:
        #     h[q].append(p)
        
        # visited = [0 for _ in range(numCourses)]
        # cur = set()
        # ans = []

        # def dfs(c):
        #     if visited[c] == 1:
        #         return True
        #     if c in cur:
        #         return False
                
        #     cur.add(c)
        #     for pre in h[c]:
        #         if not dfs(pre):
        #             return False
            
        #     cur.remove(c)
        #     ans.append(c)
        #     visited[c] = 1
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return []
        # return ans
        
