class collage:
    def __init__(self, name):
        self.name=name
        print("collage Contractor called")


class department(collage):
    def __init__(s,name,dept_name):
        collage.__init__(s,name)  # calling parent class constructor
        s.dept_name=dept_name
        print("department Contractor called")


class student(department):
    def __init__(s,name,dept_name,stud_name,stud_id):
        department.__init__(s,name,dept_name)  # calling parent class constructor
        s.stud_name=stud_name
        s.stud_id=stud_id
        print("student Contractor called")
s=student("ABC collage","CSE","Abhishek",101)
print(s.name)        # Output: ABC collage
print(s.dept_name)   # Output: CSE
print(s.stud_name)   # Output: Abhishek
print(s.stud_id)     # Output: 101
print(s.__dict__)    # Output: {'name': 'ABC collage', 'dept_name': 'CSE', 'stud_name': 'Abhishek', '
                        # 'stud_id': 101}
print("\n-----------------\n")
d=department("XYZ collage","ECE")
print(d.name)        # Output: XYZ collage
print(d.dept_name)   # Output: ECE
print(d.__dict__)    # Output: {'name': 'XYZ collage', 'dept_name': 'ECE'}
print("\n-----------------\n")
c=collage("PQR collage")
print(c.name)        # Output: PQR collage
print(c.__dict__)    # Output: {'name': 'PQR collage'}
print("\n----------------------------------------------------------------------------------------------------\n")
print(s.name)        # Output: ABC collage

    