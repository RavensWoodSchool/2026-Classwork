def linear_search(items, target):
    for index in range(len(items)):
        if items[index] == target:
            return index
    return -1


def binary_search(items, target):
    if items != merge_sort(items):
        print("The list is not in order, so it has been sorted using merge sort first.")
        items = merge_sort(items)
        print("Sorted list:", items)
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def bubble_sort(items):
    items = items.copy()
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def insertion_sort(items):
    items = items.copy()
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = current
    return items


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1
    return result


def merge_sort(items):
    if len(items) <= 1:
        return items.copy()
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    numbers = []
    print("Enter integers one at a time. Enter a negative number to finish.")
    value = get_integer("Enter a number: ")
    while value >= 0:
        numbers.append(value)
        value = get_integer("Enter a number: ")

    if len(numbers) == 0:
        print("No numbers were entered.")
        return

    print("Your list:", numbers)

    choice = ""
    while choice != "6":
        print()
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Bubble Sort")
        print("4. Insertion Sort")
        print("5. Merge Sort")
        print("6. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            target = get_integer("Enter the number to find: ")
            position = linear_search(numbers, target)
            if position == -1:
                print(target, "was not found.")
            else:
                print(target, "was found at index", position)
        elif choice == "2":
            target = get_integer("Enter the number to find: ")
            position = binary_search(numbers, target)
            if position == -1:
                print(target, "was not found.")
            else:
                print(target, "was found at index", position)
        elif choice == "3":
            print("Bubble sorted:", bubble_sort(numbers))
        elif choice == "4":
            print("Insertion sorted:", insertion_sort(numbers))
        elif choice == "5":
            print("Merge sorted:", merge_sort(numbers))
        elif choice == "6":
            print("Goodbye.")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()