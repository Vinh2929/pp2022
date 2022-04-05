# input.py: module for input
class input:
  def __init__(x, student_name = "", student_id = "", student_dob = "", course = ""):
    x.student_name   = student_name
    x.student_id    = student_id
    x.student_dob    = student_dob
    x.course = course
    x.student_list = []

  def input_student(x, student_name, student_id, student_dob, course):
    student = input(student_name, student_id, student_dob, course)
    x.student_list.append(student)

# output.py: module for curses output
class output:
  def __init__(x, student_list = ''):
    x.student_list = student_list

  def list_student(x, student_list):
    for a in student_list:
      print(f"Student Name    : {a.student_name}")
      print(f"Student ID      : {a.student_id}")
      print(f"Student DoB     : {a.student_dob}")
      for b in range(len(a.course)):
        print(f"Mark for {a.course[b][0]}   :", a.course[b][1])
      print("\n")

# domains: package for classes
class domains:
  def implement(x):
    student = input('' ,'', '' ,  0)
    student.input_student('Nguyễn Xuân Vinh', 'BI11-286', '07/02/2002', (('Math','12.78'), ('Chem','19.27'), ('Phys','12.43')))
    student.input_student('Nguyễn Phan Minh', 'BI11-999', '07/03/2002', (('Math','18.59'), ('Chem','15.55'), ('Phys','13.77')))
    student.input_student('Nguyễn Tuấn Miễn', 'BI11-500', '18/10/2002', (('Math','11.34'), ('Chem','16.67'), ('Phys','14.91')))
    display_screen = output(None)
    display_screen.list_student(student.student_list)

# main.py: main script for coordination
if __name__ == "__main__":
  main = domains()
  main.implement()