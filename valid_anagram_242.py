def validAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    seen = {}
    for ch in s1:
        seen[ch] = seen.get(ch,0)+1
    print(seen)
    for ch in s2:
        if ch not in seen:
            return False
        seen[ch] -=1
        if seen[ch]<0:
            return False
    return True
s = "aabbc"
t = "bacab"
print(validAnagram(s,t))