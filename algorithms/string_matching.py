def naive_string_matching(text, pattern):
    """Naive String Matching - O((n-m+1)*m)"""
    matches = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    
    return matches

def rabin_karp(text, pattern):
    """Rabin-Karp String Matching - O(n + m) average case"""
    matches = []
    n, m = len(text), len(pattern)
    
    if m > n:
        return matches
    
    # Prime number for hashing
    prime = 101
    base = 256
    mod = 101
    
    pattern_hash = 0
    text_hash = 0
    power = 1
    
    # Calculate hash of pattern and first window
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        text_hash = (base * text_hash + ord(text[i])) % mod
        if i < m - 1:
            power = (power * base) % mod
    
    # Slide window
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Verify actual match
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                matches.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * power) + ord(text[i + m])) % mod
            if text_hash < 0:
                text_hash += mod
    
    return matches

def knuth_morris_pratt(text, pattern):
    """Knuth-Morris-Pratt String Matching - O(n + m)"""
    matches = []
    n, m = len(text), len(pattern)
    
    if m > n or m == 0:
        return matches
    
    # Build LPS (Longest Proper Prefix which is also Suffix) array
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # Search for pattern in text
    i, j = 0, 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

def boyer_moore(text, pattern):
    """Boyer-Moore String Matching - O(n/m) best case, O(n*m) worst case
    Scans pattern from right to left and uses bad character rule to skip
    """
    matches = []
    n, m = len(text), len(pattern)
    
    if m > n or m == 0:
        return matches
    
    # Build bad character table
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    # Search
    i = 0
    while i <= n - m:
        j = m - 1
        
        # Compare pattern from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            # Pattern found
            matches.append(i)
            # Move to next potential match
            i += 1 if i + m < n else 1
        else:
            # Mismatch: skip based on bad character rule
            bad_char_shift = bad_char.get(text[i + j], m)
            i += max(1, bad_char_shift - (m - 1 - j))
    
    return matches
