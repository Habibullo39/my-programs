nums = []
t = int(input("write a target"))
howmany = int(input("How many numbers"))
i = 0
while i < howmany:
    num = int(input("write a number"))
    nums.append(num)
    i = i + 1

dou = 0

i = 0
while i < len(nums) - 1:
    j = i + 1
    while j < len(nums):
      if nums[i] + nums[j] == t:
         print([i,j],end=" ")
         dou = 1
      j = j + 1

    i = i + 1

if dou == 0:
 print("No answer")
