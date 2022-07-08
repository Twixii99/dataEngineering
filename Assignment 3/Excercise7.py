def display_student(name, age):
    print(name, age)

show_student = lambda name, age : display_student(name, age)

show_student("kamal", 22)