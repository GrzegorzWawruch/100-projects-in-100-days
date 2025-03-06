# Without list comprehension
# numbers = [1, 2 ,3 ]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# with list comprehension 1
# numbers = [1, 2, 3 ]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# with list comprehension 2
# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# with list comprehension 3
# double_list = [n*2 for n in range(1,5)]
# print(double_list)

# list comprehension with condition
# names = ["Alex", "Beth", "Caroline","Dave",  "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)


# Dictionary comprehension
# import random
# names =  ["Alex", "Beth", "Caroline","Dave",  "Eleanor", "Freddie"]
# students_scores = {name : random.randint(1, 100) for name in names}
# print(students_scores)
# passed_students = {student : students_scores[student] for student in students_scores if students_scores[student] > 60 }
# print(passed_students)

# comprehension with pandas library
    #looping through dictionaries:
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print (student_data_frame)

    #loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

    # loop through row of a data frames
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Angela":
        print(row.score)