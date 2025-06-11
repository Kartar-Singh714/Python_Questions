student_data = [
    {'name': 'Ram',
     'roll no': 21,
     'age': 31,
     'course': 'python'
     },
    {'name': 'Shyam',
     'roll no': 23,
     'age': 30,
     'course': 'java'
     }
]

# Function to add new student data
def add_new_student(datalist, name, roll, age, course):
    datalist.append(
        {'name': name,
         'roll no': roll,
         'age': age,
         'course': course
         })

def display_data(datalist):
    print(datalist)  # To print data in the list
    for data in datalist:  # To print the individual data in the list
        print(data)

#Adding Students
add_new_student(student_data, 'temba', 25, 27, 'js')
add_new_student(student_data, 'timmy', 22, 26, 'kallu')

# display all data
display_data(student_data)
