# 🚀 System Design Practices — Learn by Doing

> **Daily learning journey** — OOP fundamentals → SOLID Principles → System Design  
> Follow along, learn from the code, and grow together! 💪

---

## 👋 About This Repository

Hi! I'm **Abhi**, and this repo is my **daily learning log** where I practice and document:

- 🧱 **OOP (Object-Oriented Programming)** concepts from scratch
- 🔩 **SOLID Principles** with bad ❌ vs good ✅ design comparisons
- 🏗️ **System Design** patterns and real-world examples

Every concept has:
- A **BAD design** file showing what NOT to do
- A **GOOD design** file showing the correct approach
- **Real-world examples** so concepts stick

I post daily on **LinkedIn** and now also maintaining this GitHub so anyone can follow along and learn with me!

---

## 📁 Repository Structure

```
System-design-practices/
│
├── 📂 OOP/
│   ├── Inheritance_Single.py
│   ├── Instance_Variables.py
│   ├── Objects_Callable.py
│   ├── Overloading.py
│   ├── decorator.py
│   ├── encapsulation.py
│   ├── multiple_inheritance.py
│   ├── multuiple_level_inheritance.py
│   └── property_Decorator.py
│
├── 📂 SOLID Principles/
│   └── 📂 Single Responsibility Principle/
│       ├── Bad Example/
│       │   └── user.py
│       └── Good Example/
│           ├── database.py
│           ├── main.py
│           └── user.py
│
├── 📂 Open Close Principles/
│   ├── Bad_Example.py
│   └── Good_practices.py
│
├── 📂 Liskov Substitution Principle/
│   ├── Bad expamle/
│   │   └── bad_example.py
│   └── good practics/
│
├── 📂 Interface Segregation Principle (ISP)/
│   ├── Bad Example (ISP Violation)/
│   │   └── real-world-example.py
│   └── Good Example (ISP)/
│       ├── Real-world-problem.py
│       └── easy-good-example.py
│
└── 📂 Dependency Inversion Principle (DIP)/
    └── Real World Problem/
        ├── BAD-DESIGN.py
        └── GOOD-DESIGN.py
```

---

## 🧱 PART 1 — OOP (Object-Oriented Programming)

> **Start here if you are a beginner!**

OOP is the foundation of everything. Before learning SOLID or System Design, these concepts must be crystal clear.

| File | Concept | What You Learn |
|------|---------|----------------|
| `Instance_Variables.py` | Instance Variables | How each object has its own data |
| `Objects_Callable.py` | Callable Objects | Making objects behave like functions |
| `Inheritance_Single.py` | Single Inheritance | Child class inheriting from parent |
| `multiple_inheritance.py` | Multiple Inheritance | Class inheriting from multiple parents |
| `multuiple_level_inheritance.py` | Multi-level Inheritance | Grandparent → Parent → Child chain |
| `encapsulation.py` | Encapsulation | Hiding internal data, exposing only what's needed |
| `Overloading.py` | Method Overloading | Same method name, different behavior |
| `decorator.py` | Decorators | Adding functionality without changing code |
| `property_Decorator.py` | `@property` | Controlled access to attributes |

### 🔍 Quick OOP Example — Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance       # Private — no one can directly touch this

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance          # Controlled access

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())           # ✅ 1500
# print(account.__balance)            # ❌ Error — private!
```

---

## 🔩 PART 2 — SOLID Principles

> SOLID = 5 rules that make your code **clean, scalable, and maintainable**.

| Letter | Principle | One-Line Meaning |
|--------|-----------|-----------------|
| **S** | Single Responsibility | One class = One job |
| **O** | Open/Closed | Open for extension, Closed for modification |
| **L** | Liskov Substitution | Child class must work wherever parent is used |
| **I** | Interface Segregation | Don't force classes to implement what they don't need |
| **D** | Dependency Inversion | Depend on abstractions, not concrete classes |

---

### S — Single Responsibility Principle (SRP)

> **"A class should have only ONE reason to change."**

❌ **Bad Design** — One class doing everything:

```python
# BAD: user.py — This class is doing TOO MANY things
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"{self.name} - {self.email}"

    def save_to_database(self):
        print(f"Saving {self.name} to DB...")    # ❌ DB logic inside User class

    def send_welcome_email(self):
        print(f"Sending email to {self.email}")  # ❌ Email logic inside User class
```

✅ **Good Design** — Each class has ONE job:

```python
# user.py — Only manages user data
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# database.py — Only handles DB operations
class UserDatabase:
    def save(self, user):
        print(f"Saving {user.name} to database...")

# email.py — Only sends emails
class EmailService:
    def send_welcome(self, user):
        print(f"Sending welcome email to {user.email}")
```

📂 Code: [`SOLID Principles/Single Responsibility Principle/`](./SOLID%20Principles/Single%20Responsibility%20Principle/)

---

### O — Open/Closed Principle (OCP)

> **"Open for Extension, Closed for Modification."**  
> Add new features by writing NEW code, not by changing OLD code.

❌ **Bad Design** — Every new shape requires changing existing code:

```python
# BAD: Bad_Example.py
class AreaCalculator:
    def calculate(self, shape):
        if shape == "circle":
            return 3.14 * 5 * 5
        elif shape == "rectangle":
            return 4 * 6
        # ❌ Every new shape = modify this class!
```

✅ **Good Design** — New shapes, zero changes to existing code:

```python
# GOOD: Good_practices.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5      # ✅ New shape = new class only

class Rectangle(Shape):
    def area(self):
        return 4 * 6

class Triangle(Shape):           # ✅ Just add a new class — nothing else changes
    def area(self):
        return 0.5 * 6 * 8
```

📂 Code: [`Open Close Principles/`](./Open%20Close%20Principles/)

---

### L — Liskov Substitution Principle (LSP)

> **"Child class must be able to replace Parent class without breaking anything."**

❌ **Bad Design** — Penguin is a Bird but can't fly, so it breaks the rule:

```python
# BAD: bad_example.py
class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # ❌ BREAKS LSP!

def make_bird_fly(bird: Bird):
    bird.fly()

make_bird_fly(Penguin())    # 💥 CRASH!
```

✅ **Good Design** — Separate what can fly from what cannot:

```python
# GOOD
class Bird:
    def eat(self):
        print("Eating...")

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Sparrow(FlyingBird):    # ✅ Can fly
    pass

class Penguin(Bird):          # ✅ Is a Bird, just doesn't fly — no broken behavior
    def swim(self):
        print("Swimming...")
```

📂 Code: [`Liskov Substitution Principle/`](./Liskov%20Substitution%20Principle/)

---

### I — Interface Segregation Principle (ISP)

> **"Don't force a class to implement methods it doesn't use."**

❌ **Bad Design** — Robot is forced to implement `eat()` and `sleep()`:

```python
# BAD: real-world-example.py
class Worker:
    def work(self):
        pass
    def eat(self):
        pass
    def sleep(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working...")

    def eat(self):
        raise NotImplementedError("Robots don't eat!")   # ❌ Forced!

    def sleep(self):
        raise NotImplementedError("Robots don't sleep!") # ❌ Forced!
```

✅ **Good Design** — Split into smaller, focused interfaces:

```python
# GOOD: Real-world-problem.py
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self): pass

class HumanWorker(Workable, Eatable, Sleepable):   # ✅ Uses all
    def work(self):  print("Human working...")
    def eat(self):   print("Human eating...")
    def sleep(self): print("Human sleeping...")

class Robot(Workable):                              # ✅ Only what it needs
    def work(self):  print("Robot working...")
```

📂 Code: [`Interface Segregation Principle (ISP)/`](./Interface%20Segregation%20Principle%20(ISP)/)

---

### D — Dependency Inversion Principle (DIP)

> **"High-level modules should NOT depend on low-level modules. Both should depend on abstractions."**

This is the most powerful SOLID principle for scalable architecture.

```
❌ BAD:
Notification ──────────────► EmailService

✅ GOOD:
Notification ────────────► MessageService (Abstract)
                                  ▲
                    ┌─────────────┼──────────────┐
                    │             │              │
               EmailService  SMSService  WhatsAppService
```

❌ **Bad Design** — Notification is tightly coupled to EmailService:

```python
# BAD
class EmailService:
    def send(self, message):
        print(f"Email: {message}")

class Notification:
    def __init__(self):
        self.service = EmailService()   # ❌ HARDCODED! Can never use SMS or WhatsApp

    def send(self, message):
        self.service.send(message)
```

✅ **Good Design** — Depend on abstraction, inject any service:

```python
# GOOD
from abc import ABC, abstractmethod

# 🎯 ABSTRACTION — The contract everyone follows
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Low-level modules — all follow the contract
class EmailService(MessageService):
    def send(self, message):
        print(f"📧 Email Sent: {message}")

class SMSService(MessageService):
    def send(self, message):
        print(f"📱 SMS Sent: {message}")

class WhatsAppService(MessageService):
    def send(self, message):
        print(f"💬 WhatsApp Sent: {message}")

# High-level module — depends on abstraction, not concrete class
class Notification:
    def __init__(self, service: MessageService):
        self.service = service          # ✅ Injected from outside

    def send(self, message):
        self.service.send(message)

# ─────────────────────────────
# Usage — plug in ANY service!
# ─────────────────────────────
notification = Notification(EmailService())
notification.send("Welcome!")               # 📧 Email Sent: Welcome!

notification = Notification(SMSService())
notification.send("OTP: 123456")            # 📱 SMS Sent: OTP: 123456

notification = Notification(WhatsAppService())
notification.send("Order delivered!")       # 💬 WhatsApp Sent: Order delivered!

# ✅ Add Telegram — ZERO changes to existing code!
class TelegramService(MessageService):
    def send(self, message):
        print(f"🚀 Telegram Sent: {message}")

notification = Notification(TelegramService())
notification.send("Hello from Telegram!")
```

**Why this is powerful:**

| Problem | Without DIP | With DIP |
|---------|------------|----------|
| Add new channel | Modify Notification class | Just add new class |
| Unit testing | Can't mock EmailService | Inject mock service easily |
| Maintenance | Change Email = Change Notification | Zero impact on other classes |
| Flexibility | Stuck with one service | Swap any service at runtime |

📂 Code: [`Dependency Inversion Principle (DIP)/`](./Dependency%20Inversion%20Principle%20(DIP)/)

---

## 🧩 OOP Relationships — Quick Reference

Understanding relationships is key to reading any design diagram.

| Relationship | Symbol | Meaning | Example |
|---|---|---|---|
| **Inheritance** | IS-A | Child extends Parent | `EmailService IS-A MessageService` |
| **Association** | HAS-A | One class uses another | `Notification HAS-A MessageService` |
| **Composition** | owns | Strong ownership, child dies with parent | `Car HAS-A Engine` |
| **Aggregation** | uses | Weak ownership, child can exist alone | `Team HAS-A Player` |

---

## 🎯 Learning Path — Start Here

If you're **zero to hero**, follow this order:

```
Week 1 — OOP Basics
   └── Instance Variables → Objects → Inheritance → Encapsulation
   └── Decorators → Property → Overloading → Multiple Inheritance

Week 2 — SOLID Principles
   └── S → O → L → I → D
   └── Read BAD file first, understand the problem
   └── Then read GOOD file, understand the solution

Week 3 — Apply
   └── Design your own real-world system using these principles
   └── Think: what if requirement changes? Will my design break?
```

---

## 🔑 Key Takeaways

```
SRP  → One class, one job
OCP  → Extend, don't modify
LSP  → Child must safely replace parent
ISP  → Small interfaces > one fat interface
DIP  → Depend on abstractions, not implementations
```

---

## 🤝 Connect & Learn Together

I post **daily** on LinkedIn about:
- System Design concepts
- SOLID Principles
- Real-world coding patterns
- Interview prep

If you want to **learn together**, feel free to:
- ⭐ Star this repo
- 🍴 Fork and add your own examples
- 💬 Open an Issue or Discussion with questions
- 🔗 Connect on LinkedIn

---

## 📌 Why This Repo Exists

I believe the best way to learn is to **teach**.

Writing code is one thing. Writing it in a way that others understand — and that you yourself can revisit months later and still get — is the real skill.

Every file here is written with that goal:
> **"If someone reads this with zero context, they should walk away understanding both the problem and the solution."**

---

*Happy Learning! 🚀 — Abhi*
