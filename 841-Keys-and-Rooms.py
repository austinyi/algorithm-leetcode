class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = set()
        # def dfs(visit):
        #     if visit in visited:
        #         return
        #     else:
        #         visited.add(visit)
        #         for room in rooms[visit]:
        #             dfs(room)

        # dfs(0)
        # if len(visited) == len(rooms):
        #     return True
        # else:
        #     return False

        visited = [0]*len(rooms)
        def dfs(visit):
            if visited[visit] == 1:
                return
            else:
                visited[visit] = 1
                for room in rooms[visit]:
                    dfs(room)

        dfs(0)
        if sum(visited) == len(rooms): # return all(visited)
            return True
        else:
            return False

        
