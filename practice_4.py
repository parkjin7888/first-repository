def prepareData():
    global deptList, studentList
    matrials = Dept(100,"신소재")
    mechanics = Dept(200,"기계공학과")
    deptList= [matrials, mechanics]
    studentList = []
    studentList.append(Student(101,"신철수",matrials))
    studentList.append(Student(102,"신정철",matrials))
    studentList.append(Student(201,"기대승",mechanics))
    studentList.append(Student(202,"기정은",mechanics))

class Dept:
    def __init__(self, deptNo, name):
        self.deptNo = deptNo
        self.name = name
    def __str__(self):
        result = "("+str(self.deptNo) + " " + self.name+ ")"
        return result
       
class Student:
    def __init__(self, studentNo, name, dept):
        self.studentNo = studentNo
        self.name = name
        self.dept = dept
    def __str__(self):
        result = "("+str(self.studentNo) + " "
        result += self.name + " " + self.dept.name + ")"
        return result

def main():
    prepareData()
    print("="*10,"All Departments List")
    for dept in deptList:
        print(dept)
    print("="*10,"All Students List")
    for student in studentList:
        print(student)
main()