class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n == 0):
            return(0)
        sub_str = [[] for i in range(0, n)]
        sub_str[0] = [s[0]]
        max_len = 1
        for i in range(1, n):
            if (s[i] not in sub_str[i - 1]):
                sub_str[i] = sub_str[i - 1] + [s[i]]
            else:
                k = sub_str[i - 1].index(s[i])
                sub_str[i] = sub_str[i - 1][k + 1 : ] + [s[i]]
            max_len = max(max_len, len(sub_str[i]))
        return(max_len)

