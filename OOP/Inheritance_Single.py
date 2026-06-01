class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        print("Company Constructor called")

class Employee(Company):
    def __init__(self, name, location, emp_name, emp_id):
        # Correct way to call parent constructor
        super().__init__(name, location)       # Alternatively, 
        Company.__init__(self, name, location)  # can also be used both ways used here for demonstration


        self.emp_name = emp_name
        self.emp_id = emp_id
        print("Employee Constructor called")

e = Employee("TechCorp", "New York", "Alice", 101)
print(e.emp_id)        # Output: 101
print(e.name)          # Output: TechCorp
print(e.location)      # Output: New York

print(e.__dict__)      # Output: {'name': 'TechCorp', 'location': 'New York', 'emp_name': 'Alice', 'emp_id': 101}
print(Employee.__bases__)  # Output: (<class '__main__.Company'>,)

print("\n----------------------------------------------------------------------------------------------------\n")
c=Company("BizInc", "San Francisco")
print(c.name)        # Output: BizInc
print(c.location)    # Output: San Francisco
print(c.__dict__)    # Output: {'name': 'BizInc', 'location': 'San Francisco'}
