#kth largest element 

print "Enter list of numbers : "
array = [int(x) for x in raw_input().split(" ")]

print "Enter k :"
k = input()

def partition(arr,l,h) :
	pivot = arr[0]
	length = h-l + 1
	j = -1
	i = l
	for i in range(length):
		if arr[i] <= pivot :
			j += 1
			arr[i],arr[j] = arr[j],arr[i]
			
	arr[0],arr[j] = arr[j],arr[0]
	return j

def kthLargest(arr,l,h,k):
	m = partition(arr,l,h)
	if h - m == k-1:
		return arr[m]
	elif h - m > k -1:
		return kthLargest(arr,m+1,h,k)
	else :
		return kthLargest(arr,l,m-1,k)

print kthLargest(array,0,len(array)-1,k)