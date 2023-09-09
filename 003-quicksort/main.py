"""
Implementing quicksort separately than just having it inside of 002.

Resources:
- Wikipedia: https://en.wikipedia.org/wiki/Quicksort
- Video Explaining the Process: https://www.youtube.com/watch?v=Vtckgz38QHs
"""
def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    return i+1


def quicksort(arr: list[int], lo: int, hi: int) -> None:
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)
    

def main():
    # unordered_list: list[int] = [10, 7, 6, 8, 3, 5, 5, 1, 1, 1, -1, 0, 2, 4, 9, 5]
    unordered_list: list[int] = []
    lo: int = 0
    hi: int = len(unordered_list) - 1
    quicksort(unordered_list, lo, hi)
    print(f"Ordered list after quicksort: {unordered_list}")

if __name__ == "__main__":
    main()
