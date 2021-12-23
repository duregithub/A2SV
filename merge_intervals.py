class Solution:
    def merge(self, intervals):

        output = []
        intervals.sort()
        print(intervals)
        for i in range(len(intervals)):
            if i + 1 == len(intervals):
                continue
            if intervals[i][-1] >= intervals[i+1][0]:
                if intervals[i][-1] > intervals[i+1][-1]:
                    intervals[i+1] = [intervals[i][0], intervals[i][-1]]
                    intervals[i] = 0 
                    continue
                intervals[i+1] = [intervals[i][0], intervals[i+1][-1]]
                intervals[i] = 0

        for i in range(len(intervals)):
            if intervals[i] != 0:
                output.append(intervals[i])
        return output
               
               
        

s = Solution()
print(s.merge(

[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))


        