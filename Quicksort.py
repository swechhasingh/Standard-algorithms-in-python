print "Enter list of numbers : "
array = [int(x) for x in raw_input().split(" ")]

def partition(arr,l,h) :
	pivot = arr[l]
	j = l-1
	i = l
	for i in range(l,h+1):
		if arr[i] <= pivot :
			j += 1
			arr[i],arr[j] = arr[j],arr[i]
			
	arr[l],arr[j] = arr[j],arr[l]
	return j

def quicksort(arr,l,h) :
	if l < h :
		m = partition(arr,l,h)
		quicksort(arr,l,m-1)
		quicksort(arr,m+1,h)
	return arr

print quicksort(array,0,len(array)-1)