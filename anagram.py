def is_anagram(str1, str2):
    # Normalize: lowercase and remove spaces
    clean1 = str1.lower().replace(" ", "")
    clean2 = str2.lower().replace(" ", "")
    
    # Anagrams have the same letters, so sorted versions should match
    return sorted(clean1) == sorted(clean2)


# --- Example usage ---
print(is_anagram("listen", "silent"))          # True
print(is_anagram("hello", "world"))            # False
print(is_anagram("Dormitory", "Dirty Room"))   # True