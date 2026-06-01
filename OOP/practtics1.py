# Requirements:

# Attributes:
# name
# roll_no
# marks
# Method:
# display() → student की सारी details print करे।
# is_pass() → marks ≥ 40 हो तो Pass, वरना Fail।
class student:
    def __init__(s,name,roll,marks):
        s.name=name
        s.roll_no=roll
        s.marks=marks
    def display(s):
        print('Name=',s.name)
        print('Roll no=',s.roll_no)
        print('marks= ',s.marks)
    def is_pass(s):
        if s.marks>40:
            print("Pass")
        else:
            print("Fail")
s1=student("Abhi",1,49)
s1.display()
s1.is_pass()
s2=student("Avi",1,39)
s2.display()
s2.is_pass()