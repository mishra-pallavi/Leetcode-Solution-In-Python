# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def repeat_substring(str):
    n = len(str)
    res = 0

    for i in range(n):
        visited = [0] * 256
        for j in (i, n):
            if (visited[ord(str[j])] == True):
                break
            else:
                res = max(res,j - 1 + 1)
                visited[ord(str[j])] = True
        visited[ord(str[j])] = False

    return res


s = "abcabcbb"
response = repeat_substring(s)
print(response)
