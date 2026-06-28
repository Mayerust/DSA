class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = {}
        i = 0
        j = 0
        while i < len(s):
            if s[i] in freq:
                freq[s[i]] += 1
                i += 1
            else:
                freq[s[i]] = 1
                i += 1
        while j < len(t):
            if len(t) == len(s):
                if t[j] in freq:
                    if freq[t[j]] > 1:
                        freq[t[j]] -= 1
                        j += 1
                    elif freq[t[j]] == 1:
                        del freq[t[j]]    
                        j += 1
                else:
                    return False
            else:
                return False        
        return True            

