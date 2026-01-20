import sys
s = input()

left = 0
right = 0
count = 0
result = 0
dedup = set()

while right < len(s):
    if s[right] not in dedup:
        dedup.add(s[right])
        count += 1
        result = max(result,count)
        right += 1
    else:
        dedup.remove(s[left])
        count -= 1
        left += 1

print(result)