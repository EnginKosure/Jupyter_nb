# To test a code, a dictionary with students, lessons and exam results is needed. Write a Python code to generate below dictionary with random numbers between 35 and 100.
# {'Student-1': {'Lesson-1': 73, 'Lesson-2': 82, 'Lesson-3': 43, 'Lesson-4': 88, 'Lesson-5': 92}, 'Student-2': {'Lesson-1': 36, 'Lesson-2': 99, 'Lesson-3': 56, 'Lesson-4': 56, 'Lesson-5': 96}, 'Student-3': {'Lesson-1': 44, 'Lesson-2': 66,
#                                                                                                                                                                                                              'Lesson-3': 73, 'Lesson-4': 66, 'Lesson-5': 90}, 'Student-4': {'Lesson-1': 46, 'Lesson-2': 92, 'Lesson-3': 63, 'Lesson-4': 98, 'Lesson-5': 86}, 'Student-5': {'Lesson-1': 37, 'Lesson-2': 75, 'Lesson-3': 76, 'Lesson-4': 89, 'Lesson-5': 52}}
from random import randint

print({f'Student-{x}': {f'Lesson-{y}': randint(35, 100)
                        for y in range(1, 6)} for x in range(1, 6)})
