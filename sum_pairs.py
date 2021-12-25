class Solution:
    def maxOperations(self, nums): # exceded time limit

        
        counter = 0
        n = len(nums)
        i = 0
        j = 1
        f_flag = 0
        i_flag = 0
        nums.sort()
        while(i < n):
            
            if nums[i] + nums[-1] < k:
                i += 1
                j = i + 1
                continue
          
                

            # print("i", i)
            while(j < n):
                
                if nums[i] + nums[n//2] < k:
                    j = n//2 + 1
                    continue
                
                # print( "j" , j)
                if nums[i] + nums[j] == k:
                    nums.pop(i)
                    j -= 1
                    nums.pop(j)
                    counter += 1
                    n -= 2
                    i_flag = 1
                    # print("n" , n)
                    break
                  
                else:
                    j +=1
            
            if f_flag != i_flag:
                j = i + 1
                f_flag = 0
                i_flag = 0
                continue
            i += 1
            j = i + 1
    
        return counter
s = Solution()
print(s.maxOperations([1,2,3,4], 5)) # not solved


# n = 4
# i = 0
# j = 1

# while( i < n ):
#     while( j < n):
#         print("i", i)
#         print("j", j)
#         j += 1
#     i += 1
#     j = i + 1


        