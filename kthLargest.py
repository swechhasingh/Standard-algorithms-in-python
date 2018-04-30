#kth largest element means (length - k + 1)th smallest

print "Enter list of numbers : "
array = [int(x) for x in raw_input().split(" ")]

print "Enter k :"
k = input()

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

def kthLargest(arr,l,h,k):
	m = partition(arr,l,h)
	if m == k-1:
		return arr[m]
	elif m < k-1:
		return kthLargest(arr,m+1,h,k)
	else :
		return kthLargest(arr,l,m-1,k)

print kthLargest(array,0,len(array)-1,len(array)-k + 1)