class Solution:
    def kClosest(self, points, k):

        mydict = {}
        output = []
        keylist = []
        for i in range(len(points)):
            d = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            mydict[d] = points[i]

        for key in mydict.keys():
            keylist.append(key)

        keylist.sort()
        print(keylist)

        for i in keylist[:k]:
            output.append(mydict[i])
        
        return output


s = Solution()
print(s.kClosest([[0, 1], [1, 0]], 2))
