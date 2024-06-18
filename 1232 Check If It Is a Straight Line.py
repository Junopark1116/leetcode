class Solution:    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_points = [x[0] for x in coordinates]
        if len(set(x_points)) == 1:
            return True
        else:
            point1_x, point1_y = coordinates[0]
            point2_x, point2_y = coordinates[1]
            dy = (point1_y-point2_y)
            dx = (point1_x-point2_x)
            if dx == 0:
                dx = 1
            bias = point1_y - dy/dx * point1_x
            for i in range(2,len(coordinates)):
                point_x, point_y = coordinates[i]
                if point_y != dy/dx* point_x + bias:
                    return False
        return True
