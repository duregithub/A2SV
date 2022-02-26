class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        output = []
        
        for i in range(len(points)):
          
            d = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            points[i].insert(0, d)
            
        points.sort()
        
        for i in range(k):
          
            output.append(points[i][1:])
            
        return output

        
