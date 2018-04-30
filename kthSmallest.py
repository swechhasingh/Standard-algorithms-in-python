#kth smallest element 

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

def kthSmallest(arr,l,h,k):
	m = partition(arr,l,h)
	if m == k-1:
		return arr[m]
	elif m < k-1:
		return kthSmallest(arr,m+1,h,k)
	else :
		return kthSmallest(arr,l,m-1,k)

print kthSmallest(array,0,len(array)-1,k)