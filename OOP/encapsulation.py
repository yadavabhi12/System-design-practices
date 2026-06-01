# 1. Basic Encapsulation Example with Comments

class Bank:
    def __init__(self, account_balance):
        self.__account_balance = account_balance  # Private variable (name mangling)
        self._bank_name = "SBI"                   # Protected variable
        self.branch_code = "DEL001"               # Public variable
    
    # Public method to access private data (Getter)
    def get_balance(self):
        return self.__account_balance
    
    # Public method to modify private data (Setter) with validation
    def set_balance(self, amount):
        if amount >= 0:
            self.__account_balance = amount
        else:
            print("Balance cannot be negative!")
    
    # Protected method - meant for internal use
    def _calculate_interest(self):
        return self.__account_balance * 0.04
    
    # Public method that uses protected method internally
    def apply_interest(self):
        interest = self._calculate_interest()
        self.__account_balance += interest
        return interest

# Usage
b = Bank(1000)
print(b.get_balance())        # ✅ Correct way: 1000
print(b._bank_name)           # ⚠️ Accessible but shouldn't be used directly: SBI
print(b.branch_code)          # ✅ Public: DEL001

# print(b.__account_balance)   # ❌ Error: AttributeError
print(b.__dict__)             # Shows name mangling: {'_Bank__account_balance': 1000, ...}
print(b._Bank__account_balance) # ⚠️ Accessible but DON'T DO THIS: 1000

b.set_balance(1500)           # ✅ Secure way to modify
print(b.get_balance())        # 1500

b.set_balance(-500)           # ❌ Validation prevents negative: "Balance cannot be negative!"







# 2. Advanced Secure Banking System


class SecureBankAccount:
    def __init__(self, account_holder, initial_balance, pin):
        self.__account_balance = initial_balance
        self.__account_holder = account_holder
        self.__pin = pin                    # Highly sensitive - private
        self._account_status = "Active"     # Protected
        self.transaction_history = []       # Public
    
    # 🔒 STRONG ENCAPSULATION - Proper getters/setters
    def get_balance(self, entered_pin):
        if self.__verify_pin(entered_pin):
            return self.__account_balance
        else:
            return "Invalid PIN!"
    
    def deposit(self, amount, entered_pin):
        if self.__verify_pin(entered_pin):
            if amount > 0:
                self.__account_balance += amount
                self.transaction_history.append(f"Deposited: ${amount}")
                return f"Success! New balance: ${self.__account_balance}"
            else:
                return "Invalid amount!"
        else:
            return "Invalid PIN!"
    
    def withdraw(self, amount, entered_pin):
        if self.__verify_pin(entered_pin):
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount}")
                return f"Success! Remaining balance: ${self.__account_balance}"
            else:
                return "Insufficient funds or invalid amount!"
        else:
            return "Invalid PIN!"
    
    # 🔐 PRIVATE METHOD - Internal use only
    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    # 🛡️ PROTECTED METHOD - For subclasses/internal use
    def _update_account_status(self, status):
        self._account_status = status
    
    # 📊 PUBLIC METHOD - Safe to expose
    def get_account_summary(self):
        return {
            "holder": self.__account_holder,
            "status": self._account_status,
            "transaction_count": len(self.transaction_history)
        }

# Usage
account = SecureBankAccount("John Doe", 5000, 1234)

# ✅ Secure access
print(account.get_balance(1234))        # 5000
print(account.deposit(1000, 1234))      # Success! New balance: $6000
print(account.withdraw(2000, 1234))     # Success! Remaining balance: $4000

# ❌ Security protections
print(account.get_balance(9999))        # Invalid PIN!
print(account.withdraw(5000, 1234))     # Insufficient funds!

# ✅ Public info accessible
print(account.get_account_summary())    # {'holder': 'John Doe', 'status': 'Active', ...}

# ❌ Private data inaccessible directly
# print(account.__account_balance)      # AttributeError
# print(account.__pin)                  # AttributeError

# ⚠️ But Python encapsulation can be bypassed (UNSAFE!)
print(account.__dict__)  # Shows mangled names
# {'_SecureBankAccount__account_balance': 4000, '_SecureBankAccount__account_holder': 'John Doe', ...}

# ❌ DON'T DO THIS - Breaking encapsulation
account._SecureBankAccount__account_balance = 999999  # Direct access
print(account.get_balance(1234))  # Now shows 999999 😱








# 3. Property Decorators for Better Encapsulation

class EnhancedBankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__max_daily_withdrawal = 50000
    
    # 🔄 Using property decorators for elegant encapsulation
    @property
    def balance(self):
        """Getter - accessed like attribute but with method logic"""
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Setter - validates before setting"""
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = value
    
    @property
    def account_type(self):
        """Computed property - no setter means read-only"""
        if self.__balance > 100000:
            return "Premium"
        elif self.__balance > 50000:
            return "Gold"
        else:
            return "Standard"
    
    # Private method with business logic
    def __validate_transaction(self, amount):
        return 0 < amount <= self.__max_daily_withdrawal

# Usage
acc = EnhancedBankAccount(75000)

# ✅ Clean access using properties
print(acc.balance)        # 75000 (calls getter)
print(acc.account_type)   # "Gold" (computed property)

acc.balance = 80000       # ✅ Calls setter with validation
# acc.balance = -100      # ❌ ValueError: Balance cannot be negative!

# ❌ No direct access to private variables
# print(acc.__balance)    # AttributeError





# 4. Comparison with Java/C++



# 🐍 PYTHON vs ☕ JAVA vs 🔷 C++

"""
JAVA/C++ STRONG ENCAPSULATION:
- private/protected/public keywords
- Compiler enforcement
- Truly private - cannot access from outside
- Runtime security

PYTHON WEAK ENCAPSULATION:
- Convention-based (_protected, __private)
- Name mangling for "privacy"
- Can be bypassed easily
- Trust-based system
"""

class PythonVsJavaEncapsulation:
    def __init__(self):
        self.public_data = "Anyone can access"           # Public
        self._protected_data = "Internal use"            # Protected (convention)
        self.__private_data = "Name mangled"             # Private (mangling)
    
    def java_style_secure_method(self, sensitive_data):
        """In Java, this would be truly private"""
        # In Python, we rely on developer discipline
        encrypted_data = self.__encrypt(sensitive_data)
        return encrypted_data
    
    def __encrypt(self, data):
        """Private method - internal implementation"""
        return f"encrypted_{data}"

# 🎯 SECURITY BEST PRACTICES for Python:
"""
1. Use single underscore _ for protected (convention)
2. Use double underscore __ for private (name mangling)  
3. Implement proper getters/setters with validation
4. Use property decorators for clean syntax
5. Document intended usage clearly
6. Add input validation in methods
7. Use name mangling for sensitive data
8. Trust developers but validate in production
"""

# 🔐 REAL SECURITY in Python requires:
"""
- Input validation
- Authentication/authorization
- Encryption for sensitive data
- API rate limiting
- Audit logging
- Regular security audits
"""





# 5. Complete Secure Example



class UltimateSecureBank:
    def __init__(self, customer_id, initial_deposit):
        self.__customer_id = customer_id
        self.__balance = initial_deposit
        self.__transaction_key = self.__generate_security_key()
        self._is_verified = False
    
    def __generate_security_key(self):
        """Private method - internal security"""
        import hashlib
        return hashlib.md5(str(self.__customer_id).encode()).hexdigest()
    
    @property
    def balance(self):
        if not self._is_verified:
            return "Account verification required"
        return self.__balance
    
    def verify_account(self, security_token):
        """Multi-layer security"""
        if security_token == self.__transaction_key:
            self._is_verified = True
            return True
        return False
    
    def transfer(self, amount, security_token, recipient):
        """Secure transaction with multiple validations"""
        if not self.verify_account(security_token):
            return "Security verification failed"
        
        if amount <= 0:
            return "Invalid amount"
        
        if amount > self.__balance:
            return "Insufficient funds"
        
        self.__balance -= amount
        return f"Transfer successful! Remaining: ${self.__balance}"

# Usage
bank = UltimateSecureBank("CUST123", 10000)

print(bank.balance)  # "Account verification required"

# ✅ Proper verification
if bank.verify_account(bank._UltimateSecureBank__transaction_key):  # Don't do this in real code!
    print(bank.balance)  # 10000

# In real scenario, security token would come from secure source