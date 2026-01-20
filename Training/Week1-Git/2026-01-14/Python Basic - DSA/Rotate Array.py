import sys
from collections import deque
data = sys.stdin.read().strip().splitlines()
nums = list(map(int, data[0].split()))
k = int(data[1])
k = k % len(nums)
separated_array = deque()

while k > 0:
    separated_array.appendleft(nums.pop())
    k -= 1

separated_array.extend(nums)
print(list(separated_array))

