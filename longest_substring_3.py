# brute force approch 


# 1 start from every character
# 2 create every possible substring
# 3 Check weather substring conatins duplicate character
#  Track the max length



def ls_bf(s):
    max_lenght = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i,len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_lenght = max(max_lenght,j-i+1)
    return max_lenght if max_lenght>0 else -1
#  o(n2) time complexcity and o(n) space complexcity
print(ls_bf("abcabcab"))


#  optimal solutions using window sliding 
#  we used left/right pointer 
#  we move right and calculate max  and if we find char duplicate we move left with hic char index
# Expand right to find a larger substring.
# Move left only when duplicates appear.
# Never move either pointer backward.
# Interview answer

# I use a sliding window where left and right define the current substring without repeating characters. A dictionary stores the latest index of each character. When a duplicate appears inside the current window, I move left to one position after the previous occurrence. Since both pointers only move forward, the overall time complexity is O(n).

def ls_sliding_window(s):
    char_index = {}
    left = 0
    max_lenght  = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char]>=left:
            left = char_index[char]+1
        char_index[char] = right
        max_lenght = max(max_lenght,right-left+1)
    return max_lenght if max_lenght>0 else -1


print("optimal solutins", ls_sliding_window("abcabcab"))
