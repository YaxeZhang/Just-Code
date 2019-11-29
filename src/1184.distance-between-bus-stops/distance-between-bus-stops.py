class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        tmp = sum(distance[start:destination])
        return min(tmp, sum(distance) - tmp)