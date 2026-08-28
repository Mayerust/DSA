class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        # Count frequencies of characters in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
            
        # Determine if a palindromic permutation is possible
        odd_count = sum(1 for f in freq if f % 2 == 1)
        if n % 2 == 1 and odd_count != 1:
            return ""
        if n % 2 == 0 and odd_count != 0:
            return ""
            
        mid_char = ""
        half_freq = [0] * 26
        for i in range(26):
            if freq[i] % 2 == 1:
                mid_char = chr(i + 97)
            half_freq[i] = freq[i] // 2
            
        half_n = n // 2
        
        # Check if we can exactly match the first half of the target
        tf_count = [0] * 26
        can_form_exact = True
        for i in range(half_n):
            idx = ord(target[i]) - 97
            tf_count[idx] += 1
            
        for i in range(26):
            if tf_count[i] > half_freq[i]:
                can_form_exact = False
                break
                
        if can_form_exact:
            H = target[:half_n]
            P = H + mid_char + H[::-1]
            if P > target:
                return P
                
        # Iterate backwards to find the largest index i where we can diverge from target
        # by choosing a character strictly greater than target[i]
        for i in range(half_n - 1, -1, -1):
            # Update tf_count to represent target[:i]
            idx = ord(target[i]) - 97
            tf_count[idx] -= 1
            
            # Check if target[:i] can be formed
            can_form_prefix = True
            for j in range(26):
                if tf_count[j] > half_freq[j]:
                    can_form_prefix = False
                    break
                    
            if not can_form_prefix:
                continue
                
            # Find the smallest available character c > target[i]
            c_char = None
            for j in range(idx + 1, 26):
                if half_freq[j] - tf_count[j] > 0:
                    c_char = chr(j + 97)
                    break
                    
            if c_char is not None:
                # We found the optimal divergence point and character
                avail = [half_freq[j] - tf_count[j] for j in range(26)]
                avail[ord(c_char) - 97] -= 1
                
                rest_H_chars = []
                for j in range(26):
                    if avail[j] > 0:
                        rest_H_chars.append(chr(j + 97) * avail[j])
                        
                # Form the first half H and the full palindrome P
                H = target[:i] + c_char + "".join(rest_H_chars)
                P = H + mid_char + H[::-1]
                return P
                
        # No such permutation exists
        return ""