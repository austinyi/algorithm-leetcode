# Time: O(n^2), Space: O(n) for the point_set
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set((x, y) for x, y in points)
        min_area = float('inf')

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                # Check if diagonal forms a valid rectangle (different x and y coordinates)
                if x1 != x2 and y1 != y2:
                    # Check if the other two points exist
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0
