# Printer Interface

from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print_document(self):
        pass






# Scanner Interface

class Scanner(ABC):

    @abstractmethod
    def scan_document(self):
        pass




# Fax Interface

class Fax(ABC):

    @abstractmethod
    def fax_document(self):
        pass


# Email Interface

class EmailSender(ABC):

    @abstractmethod
    def email_document(self):
        pass





# Basic Printer

class BasicPrinter(Printer):
    """
    Only printing responsibility.
    """

    def print_document(self):
        print("Printing document...")






# Scanner Device


class ScannerDevice(Scanner):
    """
    Only scanning responsibility.
    """

    def scan_document(self):
        print("Scanning document...")






# Network Printer


class NetworkPrinter(
    Printer,
    EmailSender
):
    """
    Supports printing and email.
    """

    def print_document(self):
        print("Printing document...")

    def email_document(self):
        print("Sending document by email...")







# Smart Office Machine

class SmartOfficeMachine(
    Printer,
    Scanner,
    Fax,
    EmailSender
):
    """
    Full featured machine.
    """

    def print_document(self):
        print("Printing document...")

    def scan_document(self):
        print("Scanning document...")

    def fax_document(self):
        print("Sending fax...")

    def email_document(self):
        print("Sending email...")




# Usage  


printer = BasicPrinter()
printer.print_document()

scanner = ScannerDevice()
scanner.scan_document()

smart_machine = SmartOfficeMachine()

smart_machine.print_document()
smart_machine.scan_document()
smart_machine.fax_document()
smart_machine.email_document()







# Why This Is Better


# Every class implements
# only required methods

# No useless code

# No NotImplementedError

# Easier maintenance

# Easier testing

# More flexible architecture

# New features can be added
# without affecting old classes
# Interview Explanation'👍👍👍👍👍👍👌👌

# Problem solved by ISP:

# Without ISP:
# One huge interface forces classes
# to implement methods they don't need.

# With ISP:
# Small focused interfaces allow classes
# to depend only on functionality they use.
# Real-World Analogy
# Bad:
# A driving license that forces everyone
# to learn Car + Bike + Truck + Bus.

# Good:
# Separate licenses for separate vehicles.

# You learn only what you actually need.