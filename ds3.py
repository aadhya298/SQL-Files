import matplotlib.pyplot as plt

students_name=['Aadhya','Anamika','Aalok','Sagar','Avni','Ayush','Arshiya','Anish']
student_marks=[50,45,30,40,47,45,50,35]

# def line_chart():
#     plt.plot(students_name,student_marks, marker='o', mec='r', ms=5, color='r')
#     plt.xlabel('STUDENTS')
#     plt.ylabel('MARKS')
#     plt.show()

# line_chart()

def bar_chart():
    plt.bar(students_name,student_marks, color='r',width=0.5)
    plt.xlabel('STUDENTS')
    plt.ylabel('MARKS')
    plt.show()

bar_chart()