def n_queens(n):
    board = [-1]*n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i]-col) == abs(i-row):
                return False
        return True

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row+1)

    solve(0)
    return solutions

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