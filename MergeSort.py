
print "Enter list of numbers : "
array = [int(x) for x in raw_input().split(" ")]

def copy(a,A,l,h):
	k = l
	while k <= h:
		a[k] = A[k]
		k += 1
	return a

def merge(a,l,h,mid):
	A = [0] * (h+1)	
	i, j, k = l, mid+1, l
	while i <= mid and j <= h :
		if(a[i] <= a[j]):
			A[k] = a[i]
			i += 1
			k += 1
		else :
			A[k] = a[j] 
			j += 1
			k += 1
	while(j <= h):
		A[k] = a[j]
		j += 1
		k += 1
	while( i <= mid):
		A[k] = a[i]
		i += 1
		k += 1
	arr = copy(a,A,l,h)
	return arr

def mergeSort(arr,l,h):
	if l < h:
		if l == h-1 :
			if arr[l] > arr[h] :
				arr[l],arr[h] = arr[h],arr[l]
			return arr
		else :
			mid = (l + (h))/2
			mergeSort(arr,l,mid)
			mergeSort(arr,mid+1,h)
			arr = merge(arr,l,h,mid)
			return arr
	return arr

print mergeSort(array,0,len(array)-1)







