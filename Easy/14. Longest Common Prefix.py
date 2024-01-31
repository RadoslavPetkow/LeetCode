class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(s) for s in strs)

        common_prefix = ""
        for i in range(min_len):
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    return common_prefix

            common_prefix += current_char

        return common_prefix


