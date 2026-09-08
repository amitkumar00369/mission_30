
def sortByFrequency(s: str) -> str:
    from collections import Counter
    count = Counter(s)
    return ''.join(char * freq for char, freq in count.most_common())


#  optimal solutions



def sortCharByFreq(s):
  freq = {}
  for ch in s:
    freq[ch] = freq.get(ch,0) +1
  buckets = [[] for _ in range(len(s)+1)]
  print("asdddd",freq)
  for ch,count in freq.items():
    buckets[count].append(ch)
  print(buckets)
  ans = ""
  for count in range(len(s),0,-1):
    for ch in buckets[count]:
      ans +=ch*count
  return ans


print(sortCharByFreq("tree")) 