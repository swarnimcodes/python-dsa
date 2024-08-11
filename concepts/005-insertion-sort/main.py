"""
Insertion Sort:
Insertion sort makes a sorted list to its left
as it traverses the list. It makes space for the new
element while it traverses and puts it in its right place.

Time complexity is O(n^2)

References:
- Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort
- GIF: https://en.wikipedia.org/wiki/File:Insertion-sort-example-300px.gif
"""


def insertion_sort(arr: list[int]) -> None:
    i: int = 1
    while i < len(arr):
        j: int = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1


def main():
    # unordered_list: list[int] = [10, 7, 6, 8, 3, 1, 2, 4, 9, 5]
    unordered_list: list[int] = [
        10,
        7,
        0,
        7,
        7,
        7,
        6,
        8,
        3,
        1,
        2,
        0,
        0,
        4,
        7,
        7,
        9,
        5,
        -1,
    ]
    insertion_sort(unordered_list)
    print(f"Ordered List: {unordered_list}")


if __name__ == "__main__":
    main()
