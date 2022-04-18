import sys
import codecs
import zipfile

class input_function:
  def __init__(x, student_name = "", student_id = "", student_dob = "", courses = ""):
    x.student_name = student_name
    x.student_id = student_id
    x.student_dob = student_dob
    x.courses = courses
    x.lists = []
  
  def input_student(x, student_name, student_id, student_dob, courses):
    student = input_function(student_name, student_id, student_dob, courses)
    x.lists.append(student)
  
  def compress(x, name_of_file):
    list_files = ['students.txt', 'courses.txt', 'marks.txt']

    compression = zipfile.ZIP_DEFLATED
    z = zipfile.ZipFile(name_of_file, mode = "w")

    for file in list_files:
      z.write(file, file, compress_type = compression)
    z.close()
  
  def decompress(x):
    try:
      with zipfile.ZipFile("students.dat", "r") as zip_ref:
        zip_ref.extractall("decompress")
    except Exception as e:
      print("students.dat not found")
      print("error: ",e)
  
  def write_file(x, student):
    for a in student:
      with open("students.txt", "a+", encoding = 'utf-8') as file_1:
        file_1.write('Name          :' + a.student_name + '\n')
        file_1.write('ID            :' + a.student_id + '\n')
        file_1.write('Date of birth :' + a.student_dob + '\n')
        file_1.write("\n")
      
      with open('courses.txt', 'a+', encoding = 'utf-8') as file_2:
        file_2.write('Name         :' + a.student_name + '\n')
        for b in a.courses:
          file_2.write('Courses    :' + b[0] + '\n')
          file_2.write('\n')
      
      with open('marks.txt', 'a+', encoding = 'utf-8') as file_3:
        file_3.write('Name              :' + a.student_name + '\n')
        for b in a.courses:
          file_3.write(f'{b[0]}:' + b[1] + '\n')
          file_3.write('\n')
    file_1.close()
    file_2.close()
    file_3.close()
  
class output_function:
  def __init__(x, lists = ''):
    x.lists = lists
  
  def list_student(x, lists):
    for a in lists:
      print(f"Name            : {a.student_name}")
      print(f"Id              : {a.student_id}")
      print(f"Date Of Birth   : {a.student_dob}")
      for b in range(len(a.courses)):
        print(f"Marks of {a.courses[b][0]}   : ", a.courses[b][1])
      print("\n")

student = input_function('' ,'', '' ,  0)
student.input_student('Nguyễn Xuân Vinh', 'BI11-286', '07/02/2002', (('Math', '12.78'), ('Chem', '19.27'), ('Phys', '12.43')))
student.input_student('Nguyễn Phan Minh', 'BI11-999', '07/03/2002', (('Math', '18.59'), ('Chem', '15.55'), ('Phys', '13.77')))
student.input_student('Nguyễn Tuấn Miễn', 'BI11-500', '18/10/2002', (('Math', '11.34'), ('Chem', '16.67'), ('Phys', '14.91')))

student.write_file(student.lists)

student.compress('students.dat')
student.decompress()

display = output_function()
display.list_student(student.lists)