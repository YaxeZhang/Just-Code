class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack = set(), [0]
        while stack:
            i = stack.pop()
            visited.add(i)
            stack += [j for j in rooms[i] if j not in visited]
        return len(visited) == len(rooms)