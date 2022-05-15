class Solution:
    def countOdds(self, low: int, high: int) -> int:
       
        if high%2==0 and low%2==0:
            return ((high-low)//2)
          
        if high%2!=0 and low%2!=0:
            return ((high-low)//2)+1

        if high%2!=0 and low%2==0:
            return (((high+1)-low)//2)
        
        if high%2==0 and low%2!=0:
            return (((high+1)-low)//2)
        

x = Solution()
print(x.countOdds(7,10))

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
