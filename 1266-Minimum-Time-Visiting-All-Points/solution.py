class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        sum_time = 0
        for i in range(len(points)-1):
            x1,y1 = points[i][0],points[i][1]
            x2,y2 = points[i+1][0],points[i+1][1]
            sum_time += max(abs(y2-y1),abs(x2-x1))
        return sum_time
