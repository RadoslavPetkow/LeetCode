class Solution(object):
    def lengthOfLongestSubstring(self, s):
        list_ch = 0
        string = ""

        for ch in range(len(s)):
            if s[ch] in string:
                list_ch = max(list_ch, len(string))
                string = string[string.index(s[ch]) + 1:]

            string += s[ch]

        list_ch = max(list_ch, len(string))

        return(list_ch)