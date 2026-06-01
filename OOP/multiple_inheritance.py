







class Grandfather:
    def __init__(self):
        print("Grandfather Constructor called")
    def feature(self):
        print("Feature 1 from Grandfather")
    def property(self):
        print("Property method from Grandfather")


class Father:
     def __init__(self):
        super().__init__()   # Calling Grandfather's constructor
        print("Father Constructor called")
     def feature(self):
        print("Feature 2 from Father")
     def saveManey(self):
        print("Money method from Father")

     def property(self):
        print("Property method from father")


class Child(Father, Grandfather):
    def __init__(self):  
        super().__init__()                      #   Child(Father, Grandfather):  provides priority to Father class  than Grandfather class
        print("Child Constructor called")
    def feature(self):
        print("Feature 3 from Child")
    def job(self):
        print("Job method from Child")
c = Child()   #  Grandfather Constructor called ->  Father Constructor called  -> Child Constructor called
c.feature() # Feature 3 from Child
c.property() # Property method from father
c.saveManey() # Money method from Father
c.job() # Job method from Child





# MRO (Method Resolution Order) Concept:python
class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

class C:
    def method(self):
        print("Method from C")

# Multiple Inheritance Examples
class D(A, B, C):    # Priority: A > B > C
    pass

class E(B, C, A):    # Priority: B > C > A  
    pass

class F(C, A):       # Priority: C > A
    pass

d = D()
d.method()  # Output: "Method from A"

e = E()
e.method()  # Output: "Method from B"

f = F()
f.method()  # Output: "Method from C"






# Real-world Interview Example:python
class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via PaymentGateway")
    
    def refund(self):
        print("Refund initiated via PaymentGateway")

class PayPal:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via PayPal")
    
    def paypal_specific(self):
        print("PayPal specific feature")

class Stripe:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via Stripe")
    
    def stripe_connect(self):
        print("Stripe Connect feature")

# Multiple Payment Processor
class MultiPaymentProcessor(PayPal, Stripe, PaymentGateway):
    """
    Priority: PayPal > Stripe > PaymentGateway
    Agar PayPal mein method nahi mila, toh Stripe check hoga
    Phir PaymentGateway check hoga
    """
    def process_all(self, amount):
        self.process_payment(amount)  # PayPal wala call hoga
        self.paypal_specific()        # PayPal specific
        self.stripe_connect()         # Stripe specific

# Usage
processor = MultiPaymentProcessor()
processor.process_payment(100)    # PayPal ka method call hoga
processor.process_all(200)        # Sab methods call honge
# MRO Check Karne ka Tarika:python
class X: pass
class Y: pass  
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(A, B, Z): pass

# MRO check karo
print(M.__mro__)
# Output: (<class '__main__.M'>, <class '__main__.A'>, <class '__main__.X'>, 
#          <class '__main__.B'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)
# Advanced Interview Scenario:python
class Database:
    def connect(self):
        print("Generic Database Connection")
    
    def execute_query(self, query):
        print(f"Executing: {query}")

class MySQL:
    def connect(self):
        print("MySQL Connection established")
    
    def mysql_backup(self):
        print("MySQL Backup created")

class PostgreSQL:
    def connect(self):
        print("PostgreSQL Connection established")
    
    def postgres_vacuum(self):
        print("PostgreSQL VACUUM executed")

# Hybrid Database Manager
class HybridDB(MySQL, PostgreSQL, Database):
    """
    Priority: MySQL > PostgreSQL > Database
    """
    def test_connections(self):
        self.connect()           # MySQL ka connect() call hoga
        self.mysql_backup()      # MySQL specific
        self.postgres_vacuum()   # PostgreSQL specific
        self.execute_query("SELECT 1")  # Database class se inherit hoga

# Test
db = HybridDB()
db.test_connections()
print(HybridDB.__mro__)  # MRO dekhne ke liye
# Key Points for Interview:
# MRO Left-to-Right: class Child(A, B, C) - Priority: A > B > C

# Depth-First Search: Python MRO depth-first search karta hai

# super() #Smart Hai: super() current class ke MRO ko follow karta hai

# __mro__ Attribute: Kisi bhi class ka MRO check kar sakte hain

# Diamond Problem Solve: Python MRO diamond problem ko solve karta hai

# Final Pro Tip:python
# Always check MRO in complex inheritance
class P1: pass
class P2: pass  
class C1(P1, P2): pass
class C2(P2, P1): pass

print("C1 MRO:", C1.__mro__)
print("C2 MRO:", C2.__mro__)

# Agar conflict ho toh error aayega
# class C3(C1, C2): pass  # TypeError: Cannot create a consistent method resolution order























class papa:
    def feature1(self):
        print("Feature 1 from Papa")

    def feature2(self):
        print("Feature 2 from Papa")
class mama:
    def feature3(self):
        print("Feature 3 from Mama")

    def feature4(self):
        print("Feature 4 from Mama")

class child(papa,mama):
    def feature5(self):
        print("Feature 5 from Child")
c=child()
c.feature1()  # Feature 1 from Papa
c.feature3()  # Feature 3 from Mama
c.feature5()  # Feature 5 from Child