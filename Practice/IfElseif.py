'''Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.
'''
class Solution:
    def studentGrade(self, marks):
        
        if marks >=90:
            grade="Grade A"
        elif marks >=70:
            grade="Grade B"
        elif marks >=50:
            grade="Grade C"
        elif marks >=35:
            grade="Grade D"
        else:
            grade="Fail"
        return grade            

my_solution=Solution()

student_grade = my_solution.studentGrade(marks=int(input("enter the marks: ")))
print(student_grade)
