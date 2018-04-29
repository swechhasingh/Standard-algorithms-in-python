#partition

print "Enter list of numbers : "
array = [int(x) for x in raw_input().split(" ")]

def partition(arr) :
	pivot = arr[0]
	length = len(arr)
	j = -1
	for i in range(length):
		if arr[i] <= pivot :
			j += 1
			arr[i],arr[j] = arr[j],arr[i]
			
	arr[0],arr[j] = arr[j],arr[0]
	return j

print partition(array)

