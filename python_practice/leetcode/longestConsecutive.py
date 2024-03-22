class Solution(object):
    def longestConsecutive(nums):

        nums.sort()

        print(nums)
        if nums == []:
            return 0
        else:
            max_count = 1
            current_count = 1
            for i in range(1,len(nums)):
                print(nums[i-1], " ",nums[i])
                if nums[i-1] == nums[i]-1:
                    current_count +=1
                    if current_count >= max_count:
                        max_count = current_count
             
            return max_count

    nums=[9,1,4,7,3,-1,0,5,8,-1,6]

    print(longestConsecutive(nums))