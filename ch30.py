# Given a function that accepts unlimited arguments,
# check and count how many data types are in those arguments.
# Finally return the total in a list.


# [int, str, bool, list, tuple, dict]

def count_datatypes(*args):
    my_list = [0, 0, 0, 0, 0, 0]
    for i in args:
        if type(i) == int:
            my_list[0] += 1
        elif type(i) == str:
            my_list[1] += 1
        elif type(i) == bool:
            my_list[2] += 1
        elif type(i) == list:
            my_list[3] += 1
        elif type(i) == tuple:
            my_list[4] += 1
        elif type(i) == dict:
            my_list[5] += 1
    print(my_list)
    return my_list


count_datatypes(1, 45, "Hi", False)  # ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1)  # ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [
                1, 3], {"Brayan": 18}, 25, 23)  # ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [
                1, 2, 3], [4, 5, 6])  # ➞ [2, 0, 1, 2, 2, 0]
# If no arguments are given, return [0, 0, 0, 0, 0, 0]
