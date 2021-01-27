def main(nums,target):
	h = {}
	for i, num in enumerate(nums):
		n = target - num
		if n not in h:
			h[num] = i
		else:
			return [h[n],i]

nums = [1,3,5]
print(main(nums,6))

#i = 0 num = 1 n = 6 - 1 = 5 n ko o trong h thi suy ra h[1] = 0
#i = 1 num = 3 n = 6 - 3 = 3 n ko o trong h thi suy ra h[3] = 1
#i = 2 num = 5 n = 6 - 5 = 1 thi suy ra o trong h in ra [0,2].