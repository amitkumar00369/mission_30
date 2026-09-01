def count_char(string):
    counts = {}
    for ch in string:
       counts[ch] = counts.get(ch, 0) + 1
    return counts
print(count_char("hello world"))