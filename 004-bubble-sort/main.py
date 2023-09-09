"""
Bubble Sort:
Time complexity is O(n^2)

Sometimes referred to as sinking sort.

Is a type of comparison sort.

Usually slower than even insertion sort and selection sort.

If parallel processing is allowed, bubble sort sorts in
O(n) time, making it considerably faster than insertion and
selection sort as they do not parellelize as effectively.


References:
- Wikipedia: https://en.wikipedia.org/wiki/Bubble_sort
"""
import tqdm

def bubblesort(arr: list[int]) -> None:
    swapped: bool = True
    while swapped == True:
        swap_count: int = 0
        for i in range(0, len(arr) - 1):
            j: int = i + 1
            if arr[j] < arr[i] and j < len(arr):
                arr[j], arr[i] = arr[i], arr[j]
                swap_count += 1
        if swap_count == 0:
            swapped = False
                
def main():
    unordered_list = [10, 7, 6, 8, 3, 3, 3, 3, 1, 2, 10, 10, 10, 4, 9, 5]
    # unordered_list = [0, 0, 1, -1, -2, -100, -1000000000000000000000000000000000]
    bubblesort(unordered_list)
    print(f"Ordered List: {unordered_list}")


if __name__ == "__main__":
    main()
