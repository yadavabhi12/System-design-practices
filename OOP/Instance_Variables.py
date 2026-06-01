class Abhi :
    lastName="yadav"  #class variable
    def __init__(s,name,age) :
        s.name=name  #instance variable
        s.age=age    #instance variable
    def getAge(s):
        return s.age + 5  #instance method

    def setChangeLastName(s,newLastName): 
        s.lastName=newLastName   
    
b=Abhi("abhishek",21)
print (b.name)
print (b.age)
print (b.getAge())
print(b.lastName)  # yadav
b.lastName="kumar"  #instance variable
print(b.lastName)  # kumar
print(Abhi.lastName)  # yadav
print(Abhi.getAge(Abhi("test",30)))  # 35
print(Abhi.getAge(b)) # 26

b.setChangeLastName("singh")
print(b.lastName)  # singh
print(Abhi.lastName)  # yadav
