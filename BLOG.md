# QuickSort

##  Defention

 QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

- Always pick the first element as a pivot
- Always pick the last element as a pivot
- Pick a random element as a pivot
- Pick median as a pivot



## Algorithm
1. Consider an array, arr = [10, 80, 30, 90, 40, 50, 70],  a variable pivot, i and j with the following values:
pivot = 70 (any one element from the array can be considered as pivot element) i = -1
j = 0

2. The pivot element is compared with each element in the array starting from the element at 0th index.

3. On iteration, if the element is less than or equal to the pivot element then the value of i is incremented and elements present at position i and the element present at position jare swapped, else, if the element is greater than the pivot element, then iterate to the next element.

4. Iteration1:

Initial values: i = -1 and j = 0

Since, arr[j] < pivot so, i increments to become 0 and arr[i] and arr[j] are swapped Final values: i = 0 and j = 0
Result: [10, 80, 30, 90, 40, 50, 70]

5. Iteration2:

Initial values: i = 0 and j = 1

Since, arr[j] > pivot so just iterate to the next element Final values: i = 0 and j = 1
Result: [10, 80, 30, 90, 40, 50, 70]

6. Iteration3:

Initial values: i = 0 and j = 2

Since, arr[j] < pivot so, i increments to become 1 and arr[i] and arr[j] are swapped Final values: i = 1 and j = 2
Result: [10, 30, 80, 90, 40, 50, 70]

7. Iteration4:

Initial values: i = 1 and j = 3
Since, arr[j] > pivot so just pass to the next element Final values: i = 1 and j = 3
Result: [10, 30, 80, 90, 40, 50, 70]

8. Iteration5:

Initial values: i = 1 and j = 4

Since, arr[j] < pivot so, i increments to become 2 and arr[i] and arr[j] are swapped Final values: i = 2 and j = 4

Result: [10, 30, 40, 90, 80, 50, 70]

9. Iteration6:

Initial values: i = 2 and j = 5

Since, arr[j] < pivot so, i increments to become 3 and arr[i] and arr[j] are swapped Final values: i= 3 and j = 5
Result: [10, 30, 40, 50, 80, 90, 70]

10. Iteration7:

Initial values: i = 3 and j = 6
Since, arr[j] = pivot so, i increments to become 4 and arr[i] and arr[j] are swapped Final values: i = 4 and j = 6
Result: [10, 30, 40, 50, 70, 90, 80]

With this, we have the pivot element, 70 at the sorted position, that is, all the elements placed at the left of the pivot element are lesser than pivot element and all elements at the right of the pivot element are larger than the pivot element.
Now, applying the same process to the left and right arrays of the pivot element we get the sorted array.

Final result: [10, 30, 40, 50, 70, 80, 90]


## Explanation:

First we create a user-defined function to find the partition position and pass three parameters within it. Then we consider last element as the pivot element and place it in the pivot variable. Next, we use a pointer ‘i’ to check the greater element. Then we have used a for loop to traverse the array and compare each element with pivot element.

Then we perform a condition check if the element is smaller than pivot element then swap it with greater element pointed by i. Then we perform the swapping of element from I to j using this (array[i], array[j]) = (array[j], array[i]) statement. Next we can swap the pivot element with the greater element specified by I and return the position from where the partition is done.

Next we create another user-defined function to perform quicksort(). Inside the function, we define the statements for finding the pivot element such that element smaller than pivot are on the left and element greater than pivot are on the right. Then we perform the recursive call on the left of pivot

quickSort(array, min, sub_array - 1)
and same for the right one as well.

Finally, we take a list in the array variable and print the unsorted list first and then use QuickSort(), passing the list as parameter to perform the sorting

## Example

#### Pseudo Code

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```


## Time and Space complexity in QuickSort algorithm
Time complexities:
O(n2): This occurs when the pivot element selected is the shortest or the largest
O(n*log n): This occurs when the pivot element is the middle element.
Space complexity: O(log n)