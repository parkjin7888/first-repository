def prepareData():
    global deptList, matStudentList, mechStudentList
    
    matStudentList = []
    mechStudentList = []
    
    matStudentList.append(Student("신철수"))
    matStudentList.append(Student("신정철"))
    mechStudentList.append(Student("기대승"))
    mechStudentList.append(Student("기정은"))
    
    matrials = Dept(100,"신소재",matStudentList)
    mechanics = Dept(200,"기계공학과",mechStudentList)
    
    deptList= [matrials, mechanics]

class Dept:
    def __init__(self, deptNo, name, students):
        self.deptNo = deptNo
        self.name = name
        self.students = students
    def __str__(self):
        result = "("+str(self.deptNo) + " " + self.name+" "
        result += str(self.students) + ")"
        return result
       
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        result = "("+ self.name + ")"
        return result

def main():
    prepareData()
    print("="*10,"All Departments List")
    for dept in deptList:
        print(dept)
main()