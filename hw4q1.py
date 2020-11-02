import random
import time
from copy import deepcopy


def merge_lists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(left_sublist) and j<len(right_sublist):
		#if left value is lower than right then append it to the result
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(right_sublist[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += left_sublist[i:]
	result += right_sublist[j:]
	#return the result
	return result

def merge_sort(input_list):
	#if list contains only 1 element return it
	if len(input_list) <= 1:
		return input_list
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(input_list)/2)
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		#return the merged list using the merge_list function above
		return merge_lists(left_sublist,right_sublist)

def insertionsort(A):
    #we start loop at second element (index 1) since the first item is already sorted
    for j in range(1,len(A)):
        key = A[j] #The next item we are going to insert into the sorted section of the array

        i = j-1 #the last item we are going to compare to
        #now we keep moving the key back as long as it is smaller than the last item in the array
        while (i > -1) and key < A[i]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            i=i-1 #observe the next item for next time.
        #okay i is not greater than key means key belongs at i+1
        A[i+1] = key
    return A

if __name__ == "__main__":
	sizes = [10, 50, 75, 100, 1000, 2000, 5000, 10000]

	cases = 1000
	for n in sizes:

		# test a number of different cases for small n & divide over the full range
		if n < 1000:
			# test Merge sort
			merge_start = time.time()
			for _ in range(cases):

				# Generate sample
				sample = []
				for _ in range(n):
					sample.append(random.randint(0,  1000000))
				
				merge_sort(sample)
			merge_time = (time.time() - merge_start) / float(cases)

			insertion_start = time.time()
			for _ in range(cases):

				# Generate sample
				sample = []
				for _ in range(n):
					sample.append(random.randint(0,  1000000))
				
				insertionsort(sample)
			insertion_time = (time.time() - insertion_start) / float(cases)
		else:
			# Generate sample
			sample = []
			for _ in range(n):
				sample.append(random.randint(0,  1000000))

			merge_start = time.time()
			merge_sort(deepcopy(sample))
			merge_time = time.time() - merge_start

			insertion_start = time.time()
			insertionsort(deepcopy(sample))
			insertion_time = time.time() - insertion_start

		print("For an N of: " + str(n))
		print("Merge sort: " + str(merge_time))
		print("Insertion sort: " + str(insertion_time))
		print()

		n *= 10
	
