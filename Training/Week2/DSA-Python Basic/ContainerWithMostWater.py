import sys
data = sys.stdin.read().strip()

nums = list(map(int,data.split()))
left = 0
right = len(nums) - 1
result = 0

while left < right:
    h = min(nums[left],nums[right])
    w = right - left
    result = max(result,h*w)
    if (nums[left] < nums[right]):
        left += 1
    else:
        right -= 1

print(result)