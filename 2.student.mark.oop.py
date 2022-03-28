class student_course:
    def __init__(x, student_id, student_name, student_dob, course_id, course_name, point):
        x.student_id = student_id
        x.student_name = student_name
        x.student_dob = student_dob
        x.course_id = course_id
        x.course_name = course_name
        x.point = point  
    def input(x, student_id, student_name, student_dob, course_id, course_name, point):
        y = student_course(student_id, student_name, student_dob, course_id, course_name, point)
        list.append(y)  
    def output(x, y):
            print("Student ID     : ", y.student_id)
            print("Student Name   : ", y.student_name)
            print("Student DOB    : ", y.student_dob)
            print("Course ID      : ", y.course_id)
            print("Course Name    : ", y.course_name)
            print("Point          : ", y.point)
            print("\n")     
    def search(x, std_id):
        for i in range(list.__len__()):
            if(list[i].student_id == std_id):
                return i                                    
list = []
z = student_course('', '', '', '', '', 0)
# Input information of students and their courses here
z.input("BI11-286", "Nguyen Xuan Vinh", "07/02/2002", "1", "Math", 15)
z.input("A1", "Nguyen Van A", "1/1/2000", "2", "Chem", 20)
z.input("C3", "Le Van B", "5/5/2002", "3D", "Bio", 14)
z.input("D1", "Phạm Thị D", "18/10/2002", "L3", "Linear", 9)
# List students and their information of their courses
print("\n")
print("\nList of Students and their information about courses: \n")
for i in range(list.__len__()):    
    z.output(list[i])
# Search information of a student
print("\nHere is all the information about this student:")
s = z.search("BI11-286")
z.output(list[s])
