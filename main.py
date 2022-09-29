# ******************************
# Make your Code
# ******************************

numbers = list(map(int, input().split()))
# numbers = [5, 25, 15, 10, 0]
# print (numbers)

for i in range(len(numbers)):
	minidx = numbers.index(min(numbers[i:]))
	numbers[i], numbers[minidx] = numbers[minidx], numbers[i]
	print (numbers)
