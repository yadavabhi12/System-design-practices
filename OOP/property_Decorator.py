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
        This makes balance behave like a normal variable.
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter Method
        Called when you write --> acc.balance = amount
        Here we can add validation.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount


# ---------------------------
# Using the class
acc = BankAccount(1000)

print(acc.balance)        # 1000 → calls getter method

acc.balance = 5000        # setter is called (with validation)
print(acc.balance)        # 5000


# =====================================================================
# 🔥 REAL-LIFE EXPLANATION (Future Problem Without @property)
# =====================================================================

"""
Imagine your project was using:

    acc.balance = 5000
    print(acc.balance)

Everywhere in 100+ files.

After 3 months, your manager says:

    "Add validation so balance cannot be negative."

If you DID NOT use @property earlier,
you now have to change ALL code everywhere from:

    acc.balance
to:
    acc.get_balance()

and from:
    acc.balance = 5000
to:
    acc.set_balance(5000)

This is a HUGE problem in big projects because:

    ❌ hundreds of changes
    ❌ many errors
    ❌ old code breaks
    ❌ high risk of bugs

But with @property:

    acc.balance
    acc.balance = 5000

…always stays SAME.  
You only change the internal logic in one place, inside class.

This is the MOST IMPORTANT benefit of @property.
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
# Using the old-style class
acc_old = BankAccountOld(1000)

print(acc_old.get_balance())    # Must call getter manually

acc_old.set_balance(5000)       # Must call setter manually
print(acc_old.get_balance())    # 5000


# =====================================================================
# 📌 Final Summary (Easy to Remember)
# =====================================================================

"""
Feature                              With @property                        Without @property
---------------------------------------------------------------------------------------------------
Easy to use                          ✔ Yes                                 ❌ No
Clean syntax                         ✔ acc.balance                         ❌ acc.get_balance()
Validation                           ✔ Yes                                 ✔ Yes
Future-proof (no breaking changes)   ✔ Yes (old code works)                ❌ Must change everywhere
Recommended                          ✔ Yes                                 ❌ Old style
"""

# ============================= END OF FILE =============================
