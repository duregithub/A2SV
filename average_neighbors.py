class Solution:
    def rearrangeArray(self, nums):
        
        n = len(nums)
        s_i = 1
        flag = True
        while(s_i<n-1):
            if (nums[s_i-1] + nums[s_i+1])/2 == nums[s_i]:
                if s_i + 1 == n-1:
                     nums[s_i+1], nums[s_i] = nums[s_i], nums[s_i+1]
                     return nums

                nums[s_i+1], nums[s_i+2] = nums[s_i+2], nums[s_i+1]
                s_i += 1
                continue
            
            s_i += 1
        return nums

    


            

    



s = Solution()
print(s.rearrangeArray(

[0,12,8,14,9,13,17,15]))
        