import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle index
        mid = len(arr) // 2
        
        # Dividing the list into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sorting both halves
        merge_sort(left)
        merge_sort(right)

        # Merging the sorted halves
        i = j = k = 0
        
        # Compare elements from both lists and place them in arr
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left in left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was left in right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr

def quick_sort(arr):
    def is_sorted(a):
        """Check if array is sorted (increasing or decreasing)"""
        if len(a) <= 1:
            return True
        is_increasing = all(a[i] <= a[i+1] for i in range(len(a)-1))
        is_decreasing = all(a[i] >= a[i+1] for i in range(len(a)-1))
        return is_increasing or is_decreasing
    
    # Check if input is already sorted
    was_sorted = is_sorted(arr)
    
    def sort_arr(a):
        if len(a) <= 1:
            return a
        pivot = a[0]
        left = [x for x in a[1:] if x <= pivot]
        right = [x for x in a[1:] if x > pivot]
        return sort_arr(left) + [pivot] + sort_arr(right)
    
    result = sort_arr(arr)
    return result, was_sorted

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    first_check = True
    
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            # Return index and flag indicating if found at first check
            return mid, first_check
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        first_check = False
    
    return -1, False

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    # Start from the last internal node and move up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for last_index in range(n - 1, 0, -1):
        # Swap root (max element) with the last element
        arr[0], arr[last_index] = arr[last_index], arr[0]
        
        # Heapify the reduced heap to maintain max heap property
        heapify(arr, last_index, 0)

    return arr

def strassen_multiply(A, B):
    """Strassen's Matrix Multiplication - O(n^2.807)
    
    Note: Requires square matrices with dimensions that are powers of 2 (1, 2, 4, 8, 16, etc.)
    """
    # Convert to NumPy arrays
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(A)
    
    # Validation: Check if matrices are square and have power-of-2 dimensions
    if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        raise ValueError(f"Strassen algorithm requires square matrices. Got A: {A.shape}, B: {B.shape}")
    
    if A.shape != B.shape:
        raise ValueError(f"Matrices must be the same size. Got A: {A.shape}, B: {B.shape}")
    
    # Check if n is a power of 2
    if n & (n - 1) != 0:  # Quick check if n is NOT a power of 2
        raise ValueError(f"Matrix dimensions must be a power of 2 (1, 2, 4, 8, 16...). Got {n}x{n}")
    
    # Base case: if matrix is 1x1
    if n == 1:
        return A * B

    # Dividing the matrices into 4 sub-matrices
    mid = n // 2
    a11, a12, a21, a22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    b11, b12, b21, b22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Calculating p, q, r, s, t, u, v using Strassen's formula
    p = strassen_multiply(a11 + a22, b11 + b22)
    q = strassen_multiply(a21 + a22, b11)
    r = strassen_multiply(a11, b12 - b22)
    s = strassen_multiply(a22, b21 - b11)
    t = strassen_multiply(a11 + a12, b22)
    u = strassen_multiply(a21 - a11, b11 + b12)
    v = strassen_multiply(a12 - a22, b21 + b22)

    # Combining results to form the final matrix elements
    c11 = p + s - t + v
    c12 = r + t
    c21 = q + s
    c22 = p + r - q + u

    # Joining sub-matrices back into a single result matrix
    C = np.zeros((n, n))
    C[:mid, :mid], C[:mid, mid:], C[mid:, :mid], C[mid:, mid:] = c11, c12, c21, c22
    return C