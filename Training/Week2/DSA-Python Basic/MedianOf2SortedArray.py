import string
import sys
data = sys.stdin.read().strip().splitlines()

nums1 = list(map(int,data[0].split()))
nums2 = list(map(int,data[1].split()))
length1 = len(nums1)
length2 = len(nums2)
merged_array = list()
s = "dsa"
s = s[::-1]
print(s)
left1 = 0
left2 = 0
while left1 < length1 and left2 < length2:
    if nums1[left1] < nums2[left2]:
        merged_array.append(nums1[left1])
        left1 += 1
    else:
        merged_array.append(nums2[left2])
        left2 += 1
merged_array.extend(nums1[left1:])
merged_array.extend(nums2[left2:])

final_length = len(merged_array)

if final_length % 2 == 0:
    value = (merged_array[final_length//2] + merged_array[final_length//2 - 1]) / 2
    print("{:.5f}".format(value))
else:
    print(merged_array[final_length//2])
    