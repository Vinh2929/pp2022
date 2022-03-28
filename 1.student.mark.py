from datetime import datetime
def input_numbers_of_Students ():
    return int (input("Input numbers of students: "))
def input_numbers_of_Courses ():
    return int (input ("Input number of courses: "))
def input_Students_Information ():
    student_id = input ("Input student-id: ")
    student_name = input ("Input student name: ")
    while True:
        try:
            student_dob = input ("Input date of birth of the student dd/mm/yyyy: ")
            dob = datetime.strptime(student_dob, "%d/%m/%Y")
        except ValueError:
            print("\nThe form of this date of birth is wrong, please re-input the true form!")
            continue
        break
    True_form_dob = str(dob.day) + "/" + str(dob.month) + "/" + str(dob.year)
    return student_id, student_name, student_dob 
def input_Courses_information ():
    course_id = input ("Input course-id: ")
    course_name = input ("Input name of the course: ")
    return course_id, course_name
def input_marks (student_id, course_id):
    prompt = f"Input mark for student-id {student_id} for course-id {course_id}: ".format (student_id, course_id)
    input (prompt)
num_students = input_numbers_of_Students ()
students_list = []
for i in range (num_students):
    student_id, name, dob = input_Students_Information ()
    students_list.append ((student_id, name, dob))
num_courses = input_numbers_of_Courses ()
courses_list = []
for i in range (num_courses):
    course_id, course_name = input_Courses_information ()
    courses_list.append ((course_id, course_name))
A = {}    
while True:
  a = int (input("Input numbers of student-course marks u want to know: "))
  if a < 0 or a > num_students * num_courses:
      print("Number of student-course marks is not available, re-input availably please!")
      continue
  break 
for b in range (a):
      while True:
          student_id = input ("Input student-id: ")
          course_id = input ("Input course-id: ")
          if student_id not in [student [0] for student in students_list]:
              print ("You have not input this student-id before, please re-input the student-id you have input before!")
              continue 
          if course_id not in [course [0] for course in courses_list]:
              print ("You have not input this course-id before, please re-input the course-id you have input before!")
              continue 
          break
      while True:
          marks = float (input("Input marks: "))
          if marks < 0 or marks > 20:
              print("Mark is not available, re-input the mark please!")
              continue
          break
      if course_id in A:
          A [course_id].append ((student_id, marks))
      else:
          A [course_id] = [(student_id, marks)]
print ("\nHere is the list of all basic information about students:")
for student in students_list:
    print (f"Student id: {student[0]}; Name: {student[1]}; Date of birth: {student[2]}")
print ("\nHere is the list of all courses:")
for course in courses_list:
    print (f"Course id: {course[0]}; Name: {course[1]}")
while True:
    course_id = input ("\nWhich course-id do you want to see all the marks of the students (in that course-id)? ")
    if course_id in A:
        for C in A [course_id]:
            print (f"Student {C[0]} got marks of {C [1]}")
    else:
        print("You have not input this course-id before, please re-input the course-id you have input before!")
        continue
    break