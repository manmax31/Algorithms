# Given a sorted array of strings which is interspersed with empty strings,
# write a method to find the location of a given string.
# Assuming that the array has at least one element that is not an empty string
# Time Complexity: O(n)


def search(strings, string, first, last):
    if first > last:
        return -1
    mid = (first + last)//2

    # If mid is empty, find closest non-empty string
    if not strings[mid]:
        left = mid - 1
        right = mid + 1
        while True:
            if left < first and right > last:
                return -1
            if first <= left and strings[left]:
                mid = left
                break
            if right <= last and strings[right]:
                mid = right
                break
            right += 1
            left -= 1

    # Check for string and recurse if necessary
    if strings[mid] == string:
        return mid  # Found it
    elif strings[mid] > string:
        return search(strings, string, first, mid-1)  # Search Left
    else:
        return search(strings, string, mid+1, last)  # Search Right


def sparse_search(strings, string):
    if not strings or not string:
        return -1
    return search(strings, string, 0, len(strings)-1)


if __name__ == "__main__":
    a = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    x = "at"
    print(sparse_search(a, x))
    x = "ball"
    print(sparse_search(a, x))
    x = "car"
    print(sparse_search(a, x))
    x = "dad"
    print(sparse_search(a, x))



