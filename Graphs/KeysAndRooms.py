class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        TC : O(N+E)
        SC : O(N)
        N --> # rooms
        E --> # keys
        """
        visited = [False] * len(rooms)
        self.dfs(rooms, visited, 0)
        return all(visited)

    def dfs(self, rooms, visited, room_key):
        if not visited[room_key]:
            visited[room_key] = True
        else:
            return
        for new_room_key in rooms[room_key]:
            self.dfs(rooms, visited, new_room_key)
