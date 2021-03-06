# Sort

## Simple sorts

Efficient on small data, due to low overhead. Insertion sort is generally faster than selection sort in practice, due to fewer comparisons and good performance on almost-sorted data. But selection sortuses fewer writes.

### [Insertion sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/InsertionSort.py)

- Taking elements from the list one by one and inserting them in their correct position into a new sorted list.
- Relatively efficient for small lists and mostly sorted lists
- Insertion is expensive, requiring shifting all following elements over by one.

### [Selection sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/SelectionSort.py)

- Finds the minimum value, swaps it with the value in the first position, and repeats these steps for the remainder of the list
- It does no more than n swaps, useful when swapping is very expensive 

## Efficient sorts

Practical general sorting algorithms are almost always based on an algorithm with average time complexity (and generally worst-case complexity) O(n log n), typically heap sort, merge sort and quick sort.

Asymptotically efficient on random data, but the overhead of these algorithms becomes significant on smaller data, so often a hybrid algorithm is used, commonly switching to insertion sort once the data is small enough.

The algorithms often perform poorly on already sorted data or almost sorted data – these are common in real-world data, and can be sorted in O(n) time by appropriate algorithms.

They may also be unstable, and stability is often a desirable property in a sort. Thus more sophisticated algorithms are often employed, such as Timsort (based on merge sort) or introsort (based on quicksort, falling back to heap sort).

### [Merge sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/MergeSort.py)

- Comparing every two elements and swapping them if the first should come after the second. It then merges each of the resulting lists until at last two lists are merged into the final sorted list.

- It has additional O(n) space complexity, and involves a large number of copies in simple implementations.

### [Heap sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/HeapSort.py)

- Works by determining the largest (or smallest) element of the list, placing that at the end (or beginning) of the list, then continuing with the rest of the list, but accomplishes this task efficiently by using a data structure called a heap, a special type of binary tree. 

	Once the data list has been made into a heap, the root node is guaranteed to be the largest (or smallest) element. When it is removed and placed at the end of the list, the heap is rearranged so the largest element remaining moves to the root. Using the heap, finding the next largest element takes O(log n) time, instead of O(n) for a linear scan as in simple selection sort. 

- Much more efficient version of selection sort. 

### [Quick sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/QuickSort.py)

- A divide and conquer algorithm which relies on a partition operation: to partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it.

## Bubble sort and variants

Simple but highly inefficient sorts.

### [Bubble sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/BubbleSort.py)

- Compares the first two elements, and if the first is greater than the second, it swaps them. It continues doing this for each pair of adjacent elements(12, 23, 34, ...) to the end of the data set. Repeating until no swaps have occured on the last pass.

- This algorithm's average time and worst-case performance is O(n^2), so it is rarely used to sort large, unordered data sets.

- Can be used to sort a small number of items (where its asymptotic inefficiency is not a high penalty

### Shell sort

- Generalization of insertion sort that allows the exchange of items that are far apart.

- The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list. Such a list is said to be h-sorted. Equivalently, it can be thought of as h interleaved lists, each individually sorted.

### Comb sort

- Better version of bubble sort: initially swapping elements that are a certain distance from one another in the array, rather than only swapping elements if they are adjacent to one another, and then shrinking the chosen distance until it is operating as a normal bubble sort. 


## Distribution sort

Distribution sort refers to any sorting algorithm where data are distributed from their input to multiple intermediate structures which are then gathered and placed on the output.

### [Counting sort](https://github.com/RioAraki/Interview_prep/blob/master/topic/sort/CountingSort.py)

- Counting sort works well **only when inputs range is small and there are a lot of duplicate items.**

- The algorithm loops over the items, computing a histogram of the number of times each key occurs within the input collection. 

	It then performs a prefix sum computation (a second loop, over the range of possible keys) to determine, for each key, the starting position in the output array of the items having that key. 

	Finally, it loops over the items again, moving each item into its sorted position in the output array.

### Bucket sort

- Distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm. 


### Radix sort
