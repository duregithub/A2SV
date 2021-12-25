class Solution:

    def numIdenticalPairs(self, nums):

        i = 0
        j = i + 1
        n = len(nums)
        counter = 0
        
        while(i < n):
            
            while (j < n):
                
                if nums[i] == nums[j]:
                    counter += 1
                
                j += 1
            
            i += 1
            j = i + 1
        return counter
        
s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))