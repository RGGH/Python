#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#  |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from typing import List

nums = [3,7,5,3]
target = 12

def two_sum(nums: List[int], target: int) -> List[int]:

    for i in range (0,len(nums)):

        for j in range(1,len(nums)):
            if target - nums[j] == nums[i]:
                return(i,j)