import sys
'''
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")
# uncomment for submission
'''
s = input()
d = {} # d[char] = [list of characters that follow the element before repeating itself]
counts = {}
for x in range(len(s)):
    if s[x] in d:
        # you've seen it before
        counts[s[x]] = 2
        for y in list(d.keys()):
            if counts[y] < 2:
                d[y].append(s[x])
    else:
        # you've never seen it before
        d[s[x]] = []
        counts[s[x]] = 1
        for y in list(d.keys()):
            if y != s[x]:
                if counts[y] < 2:
                    d[y].append(s[x])

res = 0
for z in list(d.keys()):
    for i in d[z]:
        if z in d[i] and z!=i:
            res+=1
print(res//2)
