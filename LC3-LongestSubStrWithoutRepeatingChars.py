class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        l = 0
        r = 0
        maxSubStr = 0
        currSet = set()
        LEN = len(s)

        while r < LEN:
            while l < r and s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            r += 1
            maxSubStr = max(maxSubStr, len(currSet))
        return maxSubStr

