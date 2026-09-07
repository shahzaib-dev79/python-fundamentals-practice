def longest_unique_substring(s):
    seen = {}          # maps character -> most recent index
    left = 0            
    max_length = 0

    for right, char in enumerate(s):
        
        if char in seen and seen[char] >= left:
            left = seen[char] + 1   

        seen[char] = right          
        max_length = max(max_length, right - left + 1)

    return max_length


# --- Example usage ---
print("result for (abcabcbb)",longest_unique_substring("abcabcbb"))   # 3
print("result for (bbbb)",longest_unique_substring("bbbbb"))      # 1
print("result for (pwwkew)",longest_unique_substring("pwwkew"))     # 3
print("result for ("")",longest_unique_substring(""))           # 0