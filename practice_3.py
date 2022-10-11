

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