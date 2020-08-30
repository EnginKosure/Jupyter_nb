# For the sake of simplicity I'll refer to the array as "arr",
# the beginning index as "left", the end index as "right",
# and the element that we're searching for as "elem".
# The input for left and right initially will be left = 0 and right = sizeOfArray - 1.
# The rest of the algorithm can be broken down in five steps:

# If "left" > "right" then the search should end as being unsuccessful.
# Set the middle index to the floor division of ("left" + "right") / 2.
# If arr(middle) < "elem", set "left" = middle + 1 and start the algorithm over again.
# Else if arr(middle) > "elem", set "right" = middle - 1 and start the algorithm over again.
# Otherwise arr(middle) == "elem" and the item you're looking for has been found.
# Instructions
# The recursive function for this challenge will use a binary search to find an element in a given array.
# If the inputted element is found then the function should return true. If it fails to find the element then it should return false.


def binary_search(arr, left, right, elem):
    if right >= left:
        middle = (left+right)//2

        if arr[middle] == elem:
            return True

        elif arr[middle] > elem:
            return binary_search(arr, left, middle-1, elem)
        else:
            return binary_search(arr, middle + 1, right, elem)
    else:
        return False


arr = [0, 1, 2, 3, 4, 5, 6, 7,
       8, 9, 10]
elem = 7

print(binary_search(arr, 0, len(arr)-1, 7))  # ➞ True

# binary_search([1, 11, 14, 15, 32, 64, 67, 88, 92, 94], left, right, 12) ➞ False

# binary_search([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], left, right, 27) ➞ True
# Notes
# The operator for floor division in python is //.
# The array will be an int array and all integers will be positive.
# Several of the challenges that will be covered in this collection on algorithms can be solved non-recursively and without implementing the algorithms described in each challenge. I implore anyone solving these challenges to do them as intended. Not understanding the concepts taught will be an obstacle to later challenges and won't aid anyone in advancing their skills as a programmer.
# If you are stuck please check the Resources tab, Comments tab, or if you're really stuck, use the Solutions tab to unlock the answers.
