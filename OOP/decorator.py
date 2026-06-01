# =====================================================================
# 1. Using @property Decorator (Recommended Way)
# =====================================================================

class BankAccount:
    def __init__(self, balance):
        # Private variable (cannot be accessed directly outside)
        self._balance = balance

    @property
    def balance(self):
        """
        Getter Method
        Called when you write --> acc.balance
        It behaves like a normal attribute.
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter Method
        Called when you write --> acc.balance = amount
        Here validation is applied.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount


# ---------------------------
# Using the class
acc = BankAccount(1000)

print(acc.balance)        # 1000 → getter method called
acc.balance = 5000        # setter method called
print(acc.balance)        # 5000


# =====================================================================
# 🔥 REAL-LIFE EXPLANATION (WHY FUTURE CHANGE IS A PROBLEM)
# =====================================================================

"""
Imagine your entire project uses:

    acc.balance
    acc.balance = 5000

Later your boss says:

    "Add validation. Negative balance not allowed."

If you used direct variable (no @property):

    acc.balance = -100  → invalid

To fix this, you add manual getter/setter:

    acc.get_balance()
    acc.set_balance()

BUT…

Now your entire project must change:
    ALL acc.balance → acc.get_balance()
    ALL acc.balance = x → acc.set_balance(x)

This breaks old code → 100+ fixes → errors → bugs.

But with @property, your old code still works:

    acc.balance
    acc.balance = 5000

No changes needed outside the class.

This is the biggest advantage of @property.
"""


# =====================================================================
# 2. Without @property (Old Style, Not Recommended)
# =====================================================================

class BankAccountOld:
    def __init__(self, balance):
        self._balance = balance

    # Manual getter
    def get_balance(self):
        return self._balance

    # Manual setter
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount


# ----------------------------
acc_old = BankAccountOld(1000)
print(acc_old.get_balance())   # manual getter
acc_old.set_balance(5000)      # manual setter
print(acc_old.get_balance())


# =====================================================================
# 3. YOUR OLD DECORATOR EXAMPLE (Real-Life Class Decorator)
# =====================================================================

# This section helps your future-self understand
# how decorators work BEFORE learning @property.

class Decorator(object):   # object is optional
    def __init__(self, fun):     # constructor (corrected)
        self.function = fun      # store function reference

    def __call__(self, *args):
        """
        When you call add(1,2,3), Python calls this method.
        Because add = Decorator(add) after decoration.
        """
        try:
            # Check if any argument is string
            if any([isinstance(i, str) for i in args]):
                raise TypeError("Cannot pass string arguments")
            else:
                return self.function(*args)  # call original function
        except Exception as obj:
            print(f"Error: {obj}")
            return None


@Decorator
def add(*args):
    total = 0
    for i in args:
        total += i
    return total


# Testing your old decorator
print(add(1, 2, 4, 45))       # 52
print(add(1, 20, 23, 45))     # 89
print(add(1, "hello", 45))    # error (string not allowed)


"""
Python internally does:
    add = Decorator(add)

So when you call:
    add(1,2,3)

Python actually calls:
    Decorator.__call__(1,2,3)

This is how decorator works internally.
"""


# =====================================================================
# 📌 Final Summary (Easy to Remember)
# =====================================================================

"""
Feature                              With @property                        Without @property
---------------------------------------------------------------------------------------------------
Easy to use                          ✔ Yes                                 ❌ No
Clean syntax                         ✔ acc.balance                         ❌ acc.get_balance()
Validation                           ✔ Yes                                 ✔ Yes
Future-proof (no breaking changes)   ✔ Yes                                 ❌ Must change everywhere
Recommended                          ✔ Yes                                 ❌ Old style

Decorator concept:
-------------------------------------
✔ Decorator wraps a function.
✔ Your Decorator class uses __init__ + __call__.
✔ @property also internally uses decorator concept.
"""

# ============================= END OF FILE =============================
