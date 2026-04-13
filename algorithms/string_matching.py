def naive_string_matching(text, pattern):
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
    matches = []
    n, m = len(text), len(pattern)
    if m > n:
        return matches
    prime = 101
    base = 256
    mod = 101
    pattern_hash = 0
    text_hash = 0
    power = 1
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        text_hash = (base * text_hash + ord(text[i])) % mod
        if i < m - 1:
            power = (power * base) % mod
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                matches.append(i)
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * power) + ord(text[i + m])) % mod
            if text_hash < 0:
                text_hash += mod
    return matches

def knuth_morris_pratt(text, pattern):
    matches = []
    n, m = len(text), len(pattern)
    if m > n or m == 0:
        return matches
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
    matches = []
    n, m = len(text), len(pattern)
    if m > n or m == 0:
        return matches
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            i += 1 if i + m < n else 1
        else:
            bad_char_shift = bad_char.get(text[i + j], m)
            i += max(1, bad_char_shift - (m - 1 - j))
    return matches
