import math
import numpy as np

student_list = []

class Student:
  def __init__(x, student_name = "", student_id = "", student_dob = "", course = ""):
    x.student_name = student_name
    x.student_id = student_id
    x.student_dob = student_dob
    x.course = course

  def input_student(x, student_name, student_id, student_dob, course):
    student = Student(student_name, student_id, student_dob, course)
    student_list.append(student)
  
  def list_student(x, student):
    print(f'Student Name         : {student.student_name}')
    print(f'Student ID           : {student.student_id}')
    print(f'Student DoB          : {student.student_dob}')
    for a, b in student.course.items():
      print(f'Mark for {a}        : {b}')
    print('\n')
  
course_list = []

class Course:
  def __init__(x, course_id = "", course_name = ""):
    x.course_id = course_id
    x.course_name = course_name
  
  def input_course(x, course_id, course_name):
    course = Course(course_id, course_name)
    course_list.append(course)
  
  def list_course(x, course):
    print(f"Course Name          : {course.course_name}")
    print(f"Course Id            : {course.course_id}\n")
  
  def mark(x, student_name, course_name, mark):
    for i in range(len(student_list)):
      if student_name in student_list[i].student_name:
        student_list[i].course[course_name] = math.floor(mark * 10) / 10

class GPA:
  def __init__(x, student_name = ''):
    x.student_name = student_name
  
  def calculate_gpa(x, student_name, credit):
    lists = []
    for i in range(len(student_list)):
      if student_name == student_list[i].student_name:
        print(student_list[i].course)
        lists.append(student_list[i].course)
        transcript = np.array([list(z.values()) for z in lists])
        credit = np.array(credit)
        gpa = transcript.dot(credit) / sum(credit)
        return tuple((student_name, gpa))
        
    
  def sort(x):
    gpa_list = []
    for i in range(len(student_list)):
      gpa_list.append(x.calculate_gpa(student_list[i].student_name, [3, 1]))
    sorted_list = sorted(gpa_list, key = lambda i: i[1])
    for first, last in enumerate(sorted_list):
      print(f"\n#{first + 1}: {last[0]} - GPA = {last[1]}")

student = Student()
student.input_student('Nguyễn Xuân Vinh', 'BI11-286', '07/02/2002', {})
student.input_student('Nguyễn Phan Minh', 'BI11-999', '07/03/2002', {})
student.input_student('Nguyễn Tuấn Miễn', 'BI11-500', '18/10/2002', {})

courses = Course('','')
courses.input_course('M1', 'Math')
courses.input_course('C2', 'Chem')

courses.mark('Nguyễn Xuân Vinh', 'Math', 12.78)
courses.mark('Nguyễn Phan Minh', 'Math', 18.59)
courses.mark('Nguyễn Tuấn Miễn', 'Math', 11.34)

courses.mark('Nguyễn Xuân Vinh', 'Chem', 19.27)
courses.mark('Nguyễn Phan Minh', 'Chem', 15.55)
courses.mark('Nguyễn Tuấn Miễn', 'Chem', 16.67)

for i in range(len(student_list)):
  student.list_student(student_list[i])

for i in range(len(course_list)):
  courses.list_course(course_list[i])

gpa = GPA()
gpa.sort()