class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        
        # Count character frequencies in s
        for char in s:
            freq[ord(char) - 97] += 1
            
        matched = 0
        
        # Match as many characters of target as possible
        while matched < n and freq[ord(target[matched]) - 97] > 0:
            freq[ord(target[matched]) - 97] -= 1
            matched += 1
            
        # If we matched the entire target, we must diverge at a prior index 
        # because the permutation must be strictly greater than target.
        if matched == n:
            freq[ord(target[n - 1]) - 97] += 1
            i = n - 1
        else:
            i = matched
            
        # Backtrack from the maximum matchable index to find a divergence point
        while i >= 0:
            target_char_idx = ord(target[i]) - 97
            
            # Find the smallest available character that is strictly greater than target[i]
            best_c_idx = -1
            for c_idx in range(target_char_idx + 1, 26):
                if freq[c_idx] > 0:
                    best_c_idx = c_idx
                    break
                    
            if best_c_idx != -1:
                freq[best_c_idx] -= 1
                
                # Collect all remaining available characters in lexicographical (ascending) order
                remainder = []
                for c_idx in range(26):
                    if freq[c_idx] > 0:
                        remainder.append(chr(c_idx + 97) * freq[c_idx])
                        
                # Form the final result string
                return target[:i] + chr(best_c_idx + 97) + "".join(remainder)
                
            # If no character > target[i] is available, we cannot diverge at index i.
            # We backtrack: release target[i-1] back into our available pool and move left.
            if i > 0:
                freq[ord(target[i - 1]) - 97] += 1
            i -= 1
            
        return ""