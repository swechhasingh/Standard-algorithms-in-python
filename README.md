# Standard-algorithms-in-python

## 1. Binary Search
 Binary Search is used to search for a key in a sorted array. It is a Divide and conquer algorithm. 
 ###### Input : Sorted list of numbers, key
 ###### Output : index of key in list
 #### Steps
 1. Find mid point of given list.
 2. Check if number at mid is equal to key. If equal then return mid.
 3. If not equal then it will search for key in one half of the list based on these condition - 
    1. If number at mid of list is greater than key then search in first half of the list.
    2. If number at mid of list is smaller than key then search in second half of the list.
 
 
 ## 2. Partition
 
