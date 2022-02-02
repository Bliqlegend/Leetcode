def findAnagrams(s: str, p: str):
    o = []
    l = len(p)
    for i in range(len(s)):
        ts = s[i:i+l]
        if ''.join(sorted(ts)) == ''.join(sorted(p)):
            o.append(i)
    return o

def swin(s,p):
    ans = []
    hash = [0 for i in range(26)]
    phash = [0 for i in range(26)]
    window = len(s)
    length = len(p)
    if length < window:
        return ans
    left = 0
    right = 0
    while right < window:
        phash[p[right]-'a'] +=1
        hash[s[right+1]-'a'] +=1
    right-=1
    while right < length:
        if phash == hash:
            ans.append(left)
        right+=1
        if right !=length:
            hash[s[right] - 'a'] +=1
        hash[s[left]-'a'] -=1
        left+=1
    return ans


s = "abcdecdbacb"
p = "cab"

o = swin(s,p)
print(o)