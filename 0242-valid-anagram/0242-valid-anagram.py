class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False  
      freq = {}
      s.split()
      for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
      t.split()     
      for j in t:
        if j in freq:
            freq[j] -= 1
            if freq[j] < 0:
                return False
            continue
        else:
            return False
      return True                       