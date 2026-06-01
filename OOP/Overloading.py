# -------------------------------------------------------------
# REAL LIFE COMBINED EXAMPLE:
# BankAccount → Operator Overloading (+, -, >, ==)
# Payment     → Method Overloading (*args)
# -------------------------------------------------------------


class BankAccount:
    def __init__(self, owner, balance):
        # Account owner name
        self.owner = owner
        # Current balance
        self.balance = balance

    # ---------------------------------------------------------
    # 1) Addition Overloading (+)
    # ---------------------------------------------------------
    # REAL LIFE: Joint account ban raha hai (balance combine)
    #
    # VERY IMPORTANT:
    #    acc1 + acc2   → internally Python calls:
    #    acc1.__add__(acc2)
    # ---------------------------------------------------------
    def __add__(self, other):
        return BankAccount(
            owner=f"{self.owner} & {other.owner}",
            balance=self.balance + other.balance
        )

    # ---------------------------------------------------------
    # 2) Subtraction Overloading (-)
    # ---------------------------------------------------------
    # REAL LIFE: Bill pay karne ke baad balance kam ho gaya.
    #    acc1 - expense  → acc1.__sub__(expense)
    # ---------------------------------------------------------
    def __sub__(self, other):
        return BankAccount(
            owner=self.owner,
            balance=self.balance - other.balance
        )

    # ---------------------------------------------------------
    # 3) Greater-than Overloading (>)
    # ---------------------------------------------------------
    # REAL LIFE: Kaun richer? Kis account me zyada paise?
    #    acc1 > acc2 → acc1.__gt__(acc2)
    # ---------------------------------------------------------
    def __gt__(self, other):
        return self.balance > other.balance

    # ---------------------------------------------------------
    # 4) Equality Overloading (==)
    # ---------------------------------------------------------
    # REAL LIFE: Kya dono ka balance same hai?
    #    acc1 == acc2 → acc1.__eq__(acc2)
    # ---------------------------------------------------------
    def __eq__(self, other):
        return self.balance == other.balance

    # ---------------------------------------------------------
    # Display account details
    # ---------------------------------------------------------
    def __str__(self):
        return f"Owner: {self.owner}, Balance: Rs.{self.balance}"


# ---------------------------------------------------------
# METHOD OVERLOADING USING *args
# ---------------------------------------------------------
# pay() function multiple payment types handle karega.
# ---------------------------------------------------------

class Payment:

    def pay(self, *args):
        """
        Method Overloading Simulation
        pay(amount) → Cash
        pay(amount, upi) → UPI
        pay(amount, card_no, cvv) → Card
        pay(amount, bank, acc_no, ifsc) → NetBanking
        """

        if len(args) == 1:
            amount = args[0]
            print(f"Paid Rs.{amount} using Cash/Default Method.")

        elif len(args) == 2:
            amount, upi_id = args
            print(f"Paid Rs.{amount} using UPI ID: {upi_id}")

        elif len(args) == 3:
            amount, card_no, cvv = args
            print(f"Paid Rs.{amount} using Card {card_no}, CVV {cvv}")

        elif len(args) == 4:
            amount, bank, acc_no, ifsc = args
            print(f"Paid Rs.{amount} using NetBanking -> Bank: {bank}, A/C: {acc_no}, IFSC: {ifsc}")

        else:
            print("Invalid payment method.")


# ---------------------------------------------------------
# REAL LIFE SCENARIO (FULL WORKFLOW)
# ---------------------------------------------------------

print("=" * 60)
print("BANKING SYSTEM - OPERATOR OVERLOADING DEMO")
print("=" * 60)

# Create accounts
acc1 = BankAccount("Abhishek", 5000)
acc2 = BankAccount("Rohan", 3000)

print("\n1. INITIAL ACCOUNTS:")
print("Account 1:", acc1)
print("Account 2:", acc2)

# ---------------------------------------------------------
# Operator Overloading: Addition
# ---------------------------------------------------------
print("\n2. JOINT ACCOUNT CREATION USING + OPERATOR:")
joint = acc1 + acc2     # Python internally → acc1.__add__(acc2)
print("Joint Account:", joint)

# BEHIND THE SCENE EXAMPLE:
print("\n3. BEHIND THE SCENES (Manual Method Call):")
manual_joint = acc1.__add__(acc2)   # Same result as acc1 + acc2
print("Manual Call Result:", manual_joint)

# ---------------------------------------------------------
# Operator Overloading: Subtraction
# ---------------------------------------------------------
print("\n4. BILL PAYMENT USING - OPERATOR:")
expense = BankAccount("Electricity Bill", 1500)
print("Bill Amount:", expense)
remaining = acc1 - expense  # internally → acc1.__sub__(expense)
print("Remaining Balance:", remaining)

# ---------------------------------------------------------
# Comparison Overloading
# ---------------------------------------------------------
print("\n5. COMPARISON OPERATIONS:")
print("Who is richer? (acc1 > acc2):", acc1 > acc2)  # acc1.__gt__(acc2)
print("Are balances equal? (acc1 == acc2):", acc1 == acc2)  # acc1.__eq__(acc2)
print("Is acc2 richer? (acc2 > acc1):", acc2 > acc1)

# ---------------------------------------------------------
# More Operator Overloading Examples
# ---------------------------------------------------------
print("\n6. MORE OPERATOR EXAMPLES:")
acc3 = BankAccount("Priya", 5000)
print("acc1 == acc3 (same balance):", acc1 == acc3)
print("acc1 > acc3:", acc1 > acc3)

# ---------------------------------------------------------
# PAYMENT METHOD OVERLOADING OUTPUT
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("PAYMENT SYSTEM - METHOD OVERLOADING DEMO")
print("=" * 60)

p = Payment()

print("\n7. DIFFERENT PAYMENT METHODS:")
print("-" * 40)

print("Cash Payment:")
p.pay(500)                                    # Cash

print("\nUPI Payment:")
p.pay(750, "abhishek@upi")                    # UPI

print("\nCard Payment:")
p.pay(1200, "1234-5678-9012-3456", 987)       # Card

print("\nNet Banking Payment:")
p.pay(3000, "SBI", "123456789", "SBIN000123") # NetBanking

print("\nInvalid Payment:")
p.pay(100, "a", "b", "c", "d")               # Invalid

# ---------------------------------------------------------
# ADVANCED EXAMPLE: Bank Transfer System
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("BANK TRANSFER SYSTEM")
print("=" * 60)

class BankTransfer:
    def transfer(self, *args):
        """
        transfer(amount) → Default transfer
        transfer(amount, to_account) → Specific account
        transfer(amount, to_account, note) → With note
        transfer(amount, to_account, note, priority) → Priority transfer
        """
        
        if len(args) == 1:
            amount = args[0]
            print(f"Transferred Rs.{amount} using default method")
            
        elif len(args) == 2:
            amount, to_account = args
            print(f"Transferred Rs.{amount} to account: {to_account}")
            
        elif len(args) == 3:
            amount, to_account, note = args
            print(f"Transferred Rs.{amount} to {to_account} | Note: {note}")
            
        elif len(args) == 4:
            amount, to_account, note, priority = args
            print(f"PRIORITY Transfer: Rs.{amount} to {to_account} | Note: {note} | Priority: {priority}")
            
        else:
            print("Invalid transfer request")

print("\n8. BANK TRANSFER EXAMPLES:")
transfer = BankTransfer()

transfer.transfer(5000)
transfer.transfer(7500, "Rohan's Account")
transfer.transfer(10000, "Company Account", "Salary Payment")
transfer.transfer(25000, "Vendor Account", "Project Payment", "High")

# ---------------------------------------------------------
# COMPLETE BANKING WORKFLOW
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("COMPLETE BANKING WORKFLOW")
print("=" * 60)

# Create family accounts
father = BankAccount("Mr. Sharma", 25000)
mother = BankAccount("Mrs. Sharma", 18000)
son = BankAccount("Rahul Sharma", 5000)

print("\nFAMILY ACCOUNTS:")
print("Father:", father)
print("Mother:", mother) 
print("Son:", son)

# Family joint account
print("\nFAMILY JOINT ACCOUNT:")
family_account = father + mother + son
print("Family Joint Account:", family_account)

# Expense tracking
print("\nEXPENSE TRACKING:")
monthly_expenses = BankAccount("Monthly Expenses", 15000)
remaining_family = family_account - monthly_expenses
print("After Monthly Expenses:", remaining_family)

# Wealth comparison
print("\nWEALTH COMPARISON:")
print("Father richer than Mother:", father > mother)
print("Mother richer than Son:", mother > son)
print("Family total wealth:", family_account.balance)

# Payment methods for expenses
print("\nPAYING EXPENSES:")
payment = Payment()
payment.pay(5000, "groceries@upi")
payment.pay(8000, "HDFC", "987654321", "HDFC0000123")
payment.pay(2000)  # Cash payment

print("\n" + "=" * 60)
print("WORKFLOW COMPLETED SUCCESSFULLY!")
print("=" * 60)