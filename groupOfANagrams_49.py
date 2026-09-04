from collections import defaultdict
def groupOfAnagram(lw):
  

  groups = defaultdict(list)
  groups = {}

  for word in strs:
      freq = [0] * 26

      for ch in word:
          freq[ord(ch) - ord('a')] += 1
      

      groups[tuple(freq)] = groups.get(tuple(freq), []) + [word]

  return list(groups.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupOfAnagram(strs))